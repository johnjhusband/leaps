#!/usr/bin/env python3
"""Buy N shares of any TICKER in the IBKR PAPER (play-money) account, end to end.

  ⛔ AUTHORIZATION: do NOT run this unless a human explicitly told you to place THIS order
     (side + ticker + size). A question like "can you make a trade?" is NOT authorization —
     answer it, don't run this. See TRADING_AUTHORIZATION.md. Running this places a real order.

Generalized from buy_one_spy.py. Connects to the local IB Gateway (paper, port 4002), shows the
paper balance and current position, places an order, waits briefly for a fill, prints the result.

Usage:
    buy_one.py TICKER [QTY] [--limit PRICE] [--market]
    QTY defaults to 1. Default order = GTC marketable limit (1% over a delayed quote) with
    outsideRth=True, so it fills at the ask in regular hours and otherwise rests to the next session.
    --market = pure MKT (regular hours only). --limit P = explicit limit price.

Safety: refuses to run unless the gateway reports a paper account (id starts 'DU').
"""
import sys, time
from ib_async import IB, Stock, MarketOrder, LimitOrder

HOST, PORT, CLIENT_ID = "127.0.0.1", 4002, 18

args = sys.argv[1:]
if not args or args[0].startswith("-"):
    print("Usage: buy_one.py TICKER [QTY] [--limit PRICE] [--market]"); sys.exit(2)
ticker = args[0].upper()
qty = 1
limit_price = None
force_market = False
i = 1
while i < len(args):
    a = args[i]
    if a == "--limit":
        limit_price = float(args[i + 1]); i += 2
    elif a == "--market":
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
    print("REFUSING TO TRADE: no paper (DU...) account on this connection."); ib.disconnect(); sys.exit(1)
acct = paper[0]
print(f"Using PAPER account {acct}")

# --- show starting state ---
summ = {s.tag: s.value for s in ib.accountSummary(acct)
        if s.tag in ("NetLiquidation", "TotalCashValue", "BuyingPower")}
print("Balance:", {k: f"${float(v):,.2f}" for k, v in summ.items()})
stk = Stock(ticker, "SMART", "USD")
if not ib.qualifyContracts(stk):
    print(f"Could not qualify contract for {ticker} (symbol/exchange?)."); ib.disconnect(); sys.exit(1)
before = next((p for p in ib.positions(acct) if p.contract.symbol == ticker), None)
print(f"{ticker} position before:", before.position if before else 0)

# --- quote (delayed-frozen; paper has no live data sub) to size a marketable limit ---
ib.reqMarketDataType(4)
tick = ib.reqMktData(stk, "", snapshot=True)
ib.sleep(4)
def _num(x): return x if (x is not None and x == x and x > 0) else None
ref = _num(tick.ask) or _num(tick.last) or _num(tick.close) or _num(tick.marketPrice())
print(f"{ticker} quote: bid={tick.bid} ask={tick.ask} last={tick.last} close={tick.close}")

# --- place the order ---
if force_market:
    order = MarketOrder("BUY", qty)
    print(f"Placing MARKET BUY {qty} {ticker} (regular hours only) ...")
else:
    if limit_price is None:
        if ref is None:
            print("No quote available to size a limit; pass --limit PRICE or --market."); ib.disconnect(); sys.exit(1)
        limit_price = round(ref * 1.01, 2)
    order = LimitOrder("BUY", qty, limit_price, tif="GTC")
    order.outsideRth = True
    print(f"Placing MARKETABLE LIMIT BUY {qty} {ticker} @ ${limit_price} (outsideRth=True) ...")
trade = ib.placeOrder(stk, order)

# --- wait for terminal status ---
deadline = time.time() + 30
while time.time() < deadline:
    ib.sleep(1)
    if trade.orderStatus.status in ("Filled", "Cancelled", "ApiCancelled", "Inactive"):
        break

st = trade.orderStatus
print(f"\nOrder status: {st.status} | filled {st.filled} @ avg ${st.avgFillPrice or 0:.2f} | remaining {st.remaining}")
for f in trade.fills:
    e = f.execution
    print(f"  FILL: {e.shares} @ ${e.price:.2f}  {e.time}  exec {e.execId}")

after = next((p for p in ib.positions(acct) if p.contract.symbol == ticker), None)
print(f"{ticker} position after:", after.position if after else (before.position if before else 0))

ib.disconnect()
print("Done.")
