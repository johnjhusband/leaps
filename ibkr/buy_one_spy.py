#!/usr/bin/env python3
"""Buy ONE share of SPY in the IBKR PAPER (play-money) account, end to end.

Connects to the local IB Gateway running in paper mode (port 4002), shows the paper
balance and any existing SPY position, places a market order for 1 share of SPY, waits
for the fill, and prints the confirmation. Read-only proof first, then the single trade.

Usage:
    ibkr/venv/bin/python ibkr/buy_one_spy.py [QTY] [--limit PRICE]
    QTY defaults to 1. Without --limit it sends a MKT order (fills instantly in RTH;
    may sit if the market is closed). --limit sends a LMT good-til-cancel so it fills
    in paper even outside regular hours once the market reopens / on simulated fills.

Safety: refuses to run unless the gateway reports a paper account (acct id starts 'DU').
"""
import sys, time
from ib_async import IB, Stock, MarketOrder, LimitOrder

HOST, PORT, CLIENT_ID = "127.0.0.1", 4002, 17

qty = 1
limit_price = None
force_market = False
args = sys.argv[1:]
i = 0
while i < len(args):
    a = args[i]
    if a == "--limit":
        limit_price = float(args[i + 1]); i += 2
    elif a == "--market":          # force a pure MKT order (only fills during regular hours)
        force_market = True; i += 1
    else:
        qty = int(a); i += 1

ib = IB()
print(f"Connecting to IB Gateway at {HOST}:{PORT} (paper) ...")
ib.connect(HOST, PORT, clientId=CLIENT_ID, timeout=20)

# --- safety: confirm this is a paper account, not live ---
accts = ib.managedAccounts()
print(f"Logged-in accounts: {accts}")
paper = [a for a in accts if a.startswith("DU")]
if not paper:
    print("REFUSING TO TRADE: no paper (DU...) account on this connection. "
          "This guard prevents accidentally trading a live account.")
    ib.disconnect(); sys.exit(1)
acct = paper[0]
print(f"Using PAPER account {acct}")

# --- show starting state ---
summ = {s.tag: s.value for s in ib.accountSummary(acct)
        if s.tag in ("NetLiquidation", "TotalCashValue", "BuyingPower")}
print("Balance:", {k: f"${float(v):,.2f}" for k, v in summ.items()})
spy = Stock("SPY", "SMART", "USD")
ib.qualifyContracts(spy)
before = next((p for p in ib.positions(acct) if p.contract.symbol == "SPY"), None)
print("SPY position before:", before.position if before else 0)

# --- a quote, for context and to size a marketable limit ---
tick = ib.reqMktData(spy, "", snapshot=True)
ib.sleep(3)
def _num(x): return x if (x is not None and x == x and x > 0) else None   # drop NaN/None/<=0
ask  = _num(tick.ask)
ref  = ask or _num(tick.last) or _num(tick.close) or _num(tick.marketPrice())
print(f"SPY quote: bid={tick.bid} ask={tick.ask} last={tick.last} close={tick.close}")

# --- place the order ---
# Default = a MARKETABLE LIMIT with outsideRth=True: behaves like market during regular hours (fills at
# the ask) but ALSO fills in pre/post-market, where a plain MKT order would be rejected/sit. A buffer
# above the ask guarantees marketability for 1 share of a liquid ETF. --market forces a pure MKT order.
if force_market:
    order = MarketOrder("BUY", qty)
    print(f"Placing MARKET BUY {qty} SPY (regular hours only) ...")
else:
    if limit_price is None:
        if ref is None:
            print("No quote available to size a limit; pass --limit PRICE or --market."); ib.disconnect(); sys.exit(1)
        limit_price = round(ref * 1.01, 2)      # 1% over reference = marketable for 1 share
    order = LimitOrder("BUY", qty, limit_price, tif="DAY")
    order.outsideRth = True
    print(f"Placing MARKETABLE LIMIT BUY {qty} SPY @ ${limit_price} (outsideRth=True) ...")
trade = ib.placeOrder(spy, order)

# --- wait for terminal status ---
deadline = time.time() + 30
while time.time() < deadline:
    ib.sleep(1)
    st = trade.orderStatus.status
    if st in ("Filled", "Cancelled", "ApiCancelled", "Inactive"):
        break

st = trade.orderStatus
print(f"\nOrder status: {st.status} | filled {st.filled} @ avg ${st.avgFillPrice or 0:.2f} "
      f"| remaining {st.remaining}")
for f in trade.fills:
    e = f.execution
    print(f"  FILL: {e.shares} @ ${e.price:.2f}  {e.time}  exec {e.execId}")
if trade.log:
    print("Log:", "; ".join(f"{l.status}:{l.message}" for l in trade.log if l.message))

after = next((p for p in ib.positions(acct) if p.contract.symbol == "SPY"), None)
print("SPY position after:", after.position if after else (before.position if before else 0))

ib.disconnect()
print("Done.")
