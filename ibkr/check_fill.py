#!/usr/bin/env python3
"""Logs whether the resting SPY paper order has filled. Run by cron around market open.
Fill signal = account SPY position >= 1 (reliable regardless of which client placed the order)."""
import datetime
from ib_async import IB
LOG = "/root/ibkr/fill_confirmation.log"
def line(msg):
    ts = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%SZ")
    with open(LOG, "a") as f: f.write(f"{ts} {msg}\n")
    print(ts, msg)
ib = IB()
try:
    ib.connect("127.0.0.1", 4002, clientId=41, timeout=20)
except Exception as e:
    line(f"CONNECT_FAIL {type(e).__name__}"); raise SystemExit(0)
acct = (ib.managedAccounts() or ["?"])[0]
ib.reqAllOpenOrders()            # pull orders placed by any client (the resting GTC was placed under another id)
ib.reqExecutions()               # pull executions/fills account-wide
ib.sleep(2)
pos = next((p for p in ib.positions(acct) if p.contract.symbol == "SPY"), None)
held = pos.position if pos else 0
opens = [t for t in ib.openTrades() if t.contract.symbol == "SPY"]
if held and held >= 1:
    line(f"FILLED SPY position={held} avgCost={pos.avgCost:.2f}")
elif opens:
    s = opens[0].orderStatus
    line(f"RESTING SPY order status={s.status} filled={s.filled} remaining={s.remaining}")
else:
    line(f"NO_OPEN_ORDER SPY position={held}")
ib.disconnect()
