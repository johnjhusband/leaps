#!/usr/bin/env python3
"""Place the orders.csv portfolio on the IBKR PAPER account (batch fractional executor).

Reads orders.csv (ticker,dollars,...), connects to the local paper gateway (127.0.0.1:4002), and for each
row places a fractional marketable-limit BUY for the dollar amount (outsideRth so it fills any hour).
Reports EVERY name: placed / filled / skipped-with-reason. Never silently drops a name.

  ⛔ AUTHORIZATION: only run when a human explicitly told you to place these trades. See TRADING_AUTHORIZATION.md.
  SAFETY: refuses unless the connected account is paper (id starts 'DU'). Restricted tickers (restricted_tickers.txt)
  are skipped even if present.

Usage: place_orders.py ORDERS_CSV [--execute] [--max N]
       default = DRY RUN (qualify+quote, place nothing). --execute actually places. --max N limits count (testing).
"""
import sys, os, csv, time
from ib_async import IB, Stock, LimitOrder

ROOT = os.path.dirname(os.path.abspath(__file__))
HOST, PORT, CID = "127.0.0.1", 4002, 51
path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else f"{ROOT}/../orders.csv"
EXECUTE = "--execute" in sys.argv
MAX = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 10**9
SKIP = int(sys.argv[sys.argv.index("--skip") + 1]) if "--skip" in sys.argv else 0  # skip first N rows (already placed)

# foreign suffix -> (exchange, currency) for IBKR contract qualification
FX = {"PA": ("SBF", "EUR"), "SW": ("EBS", "CHF"), "DE": ("IBIS", "EUR"), "MC": ("BM", "EUR"),
      "TO": ("TSE", "CAD"), "L": ("LSE", "GBP"), "AS": ("AEB", "EUR"), "HE": ("HEX", "EUR"),
      "OL": ("OSE", "NOK"), "WA": ("WSE", "PLN")}
try:
    RESTRICTED = {l.strip().upper() for l in open(f"{ROOT}/../restricted_tickers.txt") if l.strip() and not l.startswith("#")}
except Exception:
    RESTRICTED = set()

PROBE = "--probe" in sys.argv   # place ONE test order to check if fractional is live; cancel it; exit 0 ok / 2 pending
rows = [r for r in csv.DictReader(open(path))]
ib = IB()
print(f"Connecting to paper gateway {HOST}:{PORT} ...")
ib.connect(HOST, PORT, clientId=CID, timeout=25)
accts = ib.managedAccounts()
paper = [a for a in accts if a.startswith("DU")]
if not paper:
    print(f"REFUSING: connected account(s) {accts} are not paper (DU...). No orders placed."); ib.disconnect(); sys.exit(1)
acct = paper[0]
if PROBE:
    ib.reqMarketDataType(4)
    c = Stock("NVDA", "SMART", "USD"); ib.qualifyContracts(c)
    t = ib.reqMktData(c, "", snapshot=True); ib.sleep(2)
    px = (t.ask if (t.ask and t.ask == t.ask and t.ask > 0) else (t.close or 200))
    o = LimitOrder("BUY", 1.5, round(px * 1.02, 2), tif="GTC"); o.outsideRth = True   # fractional 1.5 sh
    tr = ib.placeOrder(c, o); ib.sleep(1.5)
    msg = " ".join(l.message for l in tr.log)
    ib.cancelOrder(o); ib.sleep(0.5)
    if "10243" in msg or "Fractional" in msg:
        print("PROBE: fractional STILL PENDING (10243)"); ib.disconnect(); sys.exit(2)
    print(f"PROBE: FRACTIONAL OK (status {tr.orderStatus.status}) — ready to place"); ib.disconnect(); sys.exit(0)
print(f"PAPER account {acct} | mode={'EXECUTE' if EXECUTE else 'DRY-RUN'} | {len(rows)} rows\n")
ib.reqMarketDataType(4)   # delayed-frozen (paper has no live sub)

def contract(tk):
    if "." in tk:
        sym, suf = tk.rsplit(".", 1)
        ex, cur = FX.get(suf.upper(), ("SMART", "USD"))
        return Stock(sym, ex, cur)
    return Stock(tk, "SMART", "USD")

def num(x): return x if (x is not None and x == x and x > 0) else None

# WHOLE-SHARE mode: fractional isn't enabled for the API, so buy the closest number of WHOLE shares that
# fits each name's dollar budget (floor), and the unspent remainder accumulates to CASH. Names whose price
# exceeds their per-name budget get 0 shares -> their whole budget goes to cash (flagged, not silently dropped).
placed = filled = skipped = 0
cash = 0.0
skips = []
for r in rows[SKIP:][:MAX]:
    tk = r["ticker"]; dollars = float(r["dollars"])
    if tk.upper() in RESTRICTED:
        skipped += 1; skips.append((tk, "RESTRICTED")); print(f"  SKIP {tk}: restricted"); continue
    c = contract(tk)
    if not ib.qualifyContracts(c):
        cash += dollars; skipped += 1; skips.append((tk, f"no-qualify -> ${dollars:.0f} to cash")); print(f"  SKIP {tk}: could not qualify -> ${dollars:.0f} cash"); continue
    tick = ib.reqMktData(c, "", snapshot=True); ib.sleep(2)
    px = num(tick.ask) or num(tick.last) or num(tick.close) or num(tick.marketPrice())
    if not px:
        cash += dollars; skipped += 1; skips.append((tk, f"no-quote -> ${dollars:.0f} to cash")); print(f"  SKIP {tk}: no quote -> ${dollars:.0f} cash"); continue
    shares = int(dollars // px)            # closest whole shares that FIT the budget
    cash += dollars - shares * px          # unspent remainder -> cash
    if shares < 1:
        skipped += 1; skips.append((tk, f"price ${px:.0f} > ${dollars:.0f} budget -> ${dollars:.0f} to cash")); print(f"  SKIP {tk}: ${px:.0f} > budget -> ${dollars:.0f} cash"); continue
    lmt = round(px * 1.02, 2)
    if not EXECUTE:
        print(f"  DRY  {tk}: {shares} sh @ ~{px:.2f} = ${shares*px:.0f} (+${dollars-shares*px:.0f} cash)"); placed += 1; continue
    o = LimitOrder("BUY", shares, lmt, tif="GTC"); o.outsideRth = True
    tr = ib.placeOrder(c, o)
    ib.sleep(1.0)                          # brief: catch instant RTH fills; else rests as GTC, fills at open
    st = tr.orderStatus.status
    if st == "Filled": filled += 1
    placed += 1
    print(f"  {st:9} {tk}: {shares} sh @ lmt {lmt} = ${shares*px:.0f}")

print(f"\n{'PLACED' if EXECUTE else 'WOULD-PLACE'}: {placed} | filled: {filled} | skipped: {skipped} | CASH remainder: ${cash:,.0f}")
if skips:
    print("SKIPPED (not silently dropped):")
    for tk, why in skips: print(f"  {tk}: {why}")
ib.disconnect()
