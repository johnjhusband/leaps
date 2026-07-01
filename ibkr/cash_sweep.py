#!/usr/bin/env python3
"""Cash sweep: keep buying WHOLE shares of the most-underweight buy_list names until the remaining
cash can't afford one more share of ANY name. Closes the "whole-share ceiling" gap without waiting
on IBKR fractional. Never touches restricted tickers. Paper-guarded. --execute to place.

Underweight rank each pass = target$ - held_market_value (largest positive = most underweight).
"""
import sys, os, csv
from ib_async import IB, Stock, MarketOrder
ROOT = os.path.dirname(os.path.abspath(__file__))
HOST, PORT, CID = "127.0.0.1", 4002, 101
path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else f"{ROOT}/../orders.csv"
EXECUTE = "--execute" in sys.argv
CASH_FLOOR = float(sys.argv[sys.argv.index("--floor")+1]) if "--floor" in sys.argv else 100.0
try:
    RESTRICTED = {l.strip().upper() for l in open(f"{ROOT}/../restricted_tickers.txt") if l.strip() and not l.startswith("#")}
except Exception: RESTRICTED = set()
PRICE_CEILING = {"WM","PANW","COST"}   # Brandon avoids on price (same list as build_conviction.py)
def contract(tk): return Stock(tk.replace("-", " "), "SMART", "USD")   # US-only; foreign already dropped from universe
def num(x): return x if (x is not None and x==x and x>0) else None

target = {r["ticker"]: float(r["dollars"]) for r in csv.DictReader(open(path))
          if r["ticker"].upper() not in RESTRICTED and r["ticker"] not in PRICE_CEILING and "." not in r["ticker"]}
ib = IB(); ib.connect(HOST, PORT, clientId=CID, timeout=25); acct = ib.managedAccounts()[0]
assert acct.startswith("DU"), "NOT PAPER"
print(f"PAPER {acct} | mode={'EXECUTE' if EXECUTE else 'DRY-RUN'}")
ib.reqMarketDataType(4)
# cash available (paper acct: TotalCashValue is real, big — we cap sweep to $200k-notional's leftover)
summ = {s.tag:s.value for s in ib.accountSummary(acct)}
pos = {p.contract.symbol:p for p in ib.positions(acct) if p.position!=0}
# normalize: BF-B -> "BF B" in target vs "BF B" in positions
sym2tk = {contract(tk).symbol: tk for tk in target}

# get a price per target name (delayed-frozen; paper has no live sub)
prices = {}
tickers_reqs = {}
for tk in target:
    c = contract(tk); ib.qualifyContracts(c)
    tickers_reqs[tk] = (c, ib.reqMktData(c, "", snapshot=True))
ib.sleep(6)
for tk, (c, t) in tickers_reqs.items():
    px = num(t.last) or num(t.close) or num(getattr(t,'marketPrice',lambda: None)())
    if px: prices[tk] = px
# current holdings market value in orders-ticker space (includes SGOV once, via `target` keys)
held_mv = {}
for sym, p in pos.items():
    tk = sym2tk.get(sym, sym)
    if tk in prices: held_mv[tk] = p.position * prices[tk]

# sweep budget = target notional - current securities MV. held_mv already includes SGOV
# (SGOV is a row in orders.csv, so sym2tk maps it and prices has its snapshot).
target_total = sum(target.values())          # ~200k (stocks + SGOV row)
sec_mv = sum(held_mv.values())
budget = target_total - sec_mv
print(f"target ${target_total:,.0f} | securities ${sec_mv:,.0f} | sweep budget ${budget:,.0f}")

placed = 0
while True:
    # rank underweight = target - current_mv for names in target with a price
    cands = []
    for tk, tgt in target.items():
        if tk == "SGOV": continue
        if tk not in prices: continue
        gap = tgt - held_mv.get(tk, 0)
        if gap > 0 and budget >= prices[tk]:               # any underweight, and we can afford one share
            cands.append((gap, tk))
    if not cands: break
    cands.sort(reverse=True)                                # most underweight first
    _, tk = cands[0]
    px = prices[tk]
    c = contract(tk)
    if EXECUTE:
        o = MarketOrder("BUY", 1, tif="GTC")   # market order per John's directive
        tr = ib.placeOrder(c, o); ib.sleep(0.5)
        status = tr.orderStatus.status
    else:
        status = "DRY"
    print(f"  BUY {tk} 1 sh @ ~${px:.2f} = ${px:.0f}  [{status}]  (was underweight ${target[tk]-held_mv.get(tk,0):.0f})")
    held_mv[tk] = held_mv.get(tk, 0) + px
    budget -= px
    placed += 1
    if budget < CASH_FLOOR: break
    if placed > 300: break                                  # safety

print(f"\n{'PLACED' if EXECUTE else 'WOULD-PLACE'} {placed} single-share buys | remaining budget ${budget:,.0f}")
ib.disconnect()
