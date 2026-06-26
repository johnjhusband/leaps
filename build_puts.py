#!/usr/bin/env python3
"""Phase 4 (prep) — the put-selling overlay (BUY_DECISION.md §E), with real LEAPS quotes.

Takes the top-conviction undervalued names from buy_list.csv, pulls ~2yr LEAPS put chains, picks a
strike ~10% below spot, and sizes how many puts to sell so total ASSIGNMENT VALUE (cash owed if every
sold put were assigned) stays under a regime cap of 7-day liquidity (~capital). Reports premium
collected and how to recycle it (shares + barely-OTM calls on the table-pounders).

Usage: python3 build_puts.py [CAPITAL] [ASSIGN_CAP_FRAC]
       CAPITAL default 100000 ; ASSIGN_CAP_FRAC default 0.45 (market roughly fair -> mid of 0-50% lofty band).
"""
import sys, csv, os, datetime
import yfinance as yf
ROOT = os.path.dirname(os.path.abspath(__file__))
CAPITAL = float(sys.argv[1]) if len(sys.argv) > 1 else 100_000.0
CAP_FRAC = float(sys.argv[2]) if len(sys.argv) > 2 else 0.45
today = datetime.date.today()

# put-sell candidates = the "table-pounders": already on the buy list (undervalued+reliable+moat), with a
# real moat, US-listed (deep liquid LEAPS chains), ranked by MARKET CAP (largest = most liquid, the names
# Brandon actually sells puts on — NVDA/MSFT/GOOG/AMZN/META...). Raw golden_pct is NOT the ranker: tiny-base
# EPS years make it spike to artifact levels (MRK ~4600%), which are not "deepest conviction".
rows = list(csv.DictReader(open(f"{ROOT}/buy_list.csv")))
def mc(r):
    try: return float(r.get("mktcap_B") or 0)
    except: return 0
def gp(r):
    try: return float(r.get("golden_pct") or 0)
    except: return 0
PRICE_CEILING = {"WM", "PANW", "COST"}     # Brandon avoids on price (same as build_conviction.py)
try:                                        # RESTRICTED — never tradable (insider list, e.g. MSFT)
    RESTRICTED = {l.strip().upper() for l in open(f"{ROOT}/restricted_tickers.txt")
                  if l.strip() and not l.startswith("#")}
except Exception:
    RESTRICTED = set()
cand = [r for r in rows if r.get("moat") == "yes" and "." not in r["ticker"]
        and r["ticker"].upper() not in RESTRICTED
        and r["ticker"] not in PRICE_CEILING and gp(r) <= 300]   # = the concentration sleeve, US-listed
cand.sort(key=mc, reverse=True)
cand = cand[:8]

def leaps_put(t):
    tk = yf.Ticker(t)
    spot = tk.fast_info.get("lastPrice") or tk.info.get("currentPrice")
    exps = tk.options
    if not spot or not exps:
        return None
    exp = min(exps, key=lambda e: abs((datetime.date.fromisoformat(e) - today).days - 730))
    puts = tk.option_chain(exp).puts
    K = spot * 0.90
    puts = puts.assign(dist=(puts["strike"] - K).abs()).sort_values("dist")
    row = puts.iloc[0]
    bid = float(row["bid"]) or float(row["lastPrice"])
    return {"spot": float(spot), "exp": exp, "days": (datetime.date.fromisoformat(exp) - today).days,
            "strike": float(row["strike"]), "bid": bid, "prem": bid * 100, "assign": float(row["strike"]) * 100}

assign_cap = CAPITAL * CAP_FRAC
print(f"Capital ${CAPITAL:,.0f} | assignment-value cap {CAP_FRAC:.0%} of 7-day liquidity = ${assign_cap:,.0f}")
print(f"(market-regime dial: 0-50% lofty, up to ~75% cheap — pass a different ASSIGN_CAP_FRAC to change)\n")
print(f"{'TKR':5}{'spot':>9}{'exp':>12}{'strike':>8}{'bid':>7}{'prem/ct':>9}{'assign/ct':>11}")
plan, assign_used, prem_total = [], 0.0, 0.0
for r in cand:
    t = r["ticker"]
    try:
        q = leaps_put(t)
    except Exception as e:
        print(f"{t:5}  chain error: {str(e)[:40]}"); continue
    if not q:
        print(f"{t:5}  no LEAPS chain"); continue
    # sell 1 contract if it still fits under the cap
    if assign_used + q["assign"] <= assign_cap:
        n = 1
        assign_used += q["assign"]; prem_total += q["prem"]
        plan.append((t, n, q))
        print(f"{t:5}{q['spot']:9.2f}{q['exp']:>12}{q['strike']:8.0f}{q['bid']:7.2f}{q['prem']:9.0f}{q['assign']:11.0f}  SELL {n}")
    else:
        print(f"{t:5}{q['spot']:9.2f}{q['exp']:>12}{q['strike']:8.0f}{q['bid']:7.2f}{q['prem']:9.0f}{q['assign']:11.0f}  (skip-over cap)")

print(f"\nSELL {len(plan)} puts | assignment value ${assign_used:,.0f} "
      f"({assign_used/CAPITAL:.0%} of capital) | premium collected ${prem_total:,.0f}")

# --- recycle the premium: ~50% shares of the undervalued names + ~50% barely-OTM ~2yr calls on the #1 table-pounder ---
to_shares = prem_total * 0.50
to_calls = prem_total * 0.50
print(f"\nRECYCLE ${prem_total:,.0f} premium (BUY_DECISION.md §E.2/E.3):")
print(f"  ~${to_shares:,.0f} -> BUY undervalued shares (top buy-list names, esp. the put underlyings).")
def barely_otm_call(t, otm=1.05):
    tk = yf.Ticker(t); spot = tk.fast_info.get("lastPrice") or tk.info.get("currentPrice")
    exp = min(tk.options, key=lambda e: abs((datetime.date.fromisoformat(e) - today).days - 730))
    calls = tk.option_chain(exp).calls
    K = spot * otm
    calls = calls.assign(dist=(calls["strike"] - K).abs()).sort_values("dist")
    row = calls.iloc[0]
    ask = float(row["ask"]) or float(row["lastPrice"])
    return spot, exp, float(row["strike"]), ask, ask * 100
try:
    t = plan[0][0] if plan else "NVDA"
    spot, exp, K, ask, cost = barely_otm_call(t)
    nctr = to_calls / cost if cost else 0
    print(f"  ~${to_calls:,.0f} -> BUY barely-OTM ~2yr calls on {t}: {exp} ${K:.0f} call @ ~${ask:.2f} "
          f"(${cost:,.0f}/contract) -> ~{nctr:.1f} contract(s). Buy AFTER a dip for a cheaper entry (§E.6).")
except Exception as e:
    print(f"  ~${to_calls:,.0f} -> barely-OTM ~2yr calls on the #1 table-pounder (chain fetch failed: {str(e)[:40]}).")
