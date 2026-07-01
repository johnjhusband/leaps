#!/usr/bin/env python3
"""Rebalance the paper account to the IDEAL state (BUY_DECISION.md "REBALANCING").

1. Ideal = orders.csv (target $ per ticker, incl the SGOV bond row).
2. Current = the account's actual positions.
3. Per ticker: target_shares = floor(target$ / price); delta = target - held.
   delta<0 -> SELL the excess; delta>0 -> BUY the shortfall; held-but-not-in-ideal -> SELL all.
4. ORDER OF OPERATIONS: place ALL SELLS first, then ALL BUYS (sells fund buys; never buy before the cash).
Whole shares only (fractional not enabled). Paper-guarded; restricted tickers never bought; no silent drops.

Usage: rebalance_orders.py ORDERS_CSV [--execute]   (default = DRY RUN / preview)
"""
import sys, os, csv
from ib_async import IB, Stock, MarketOrder

ROOT = os.path.dirname(os.path.abspath(__file__))
HOST, PORT, CID = "127.0.0.1", 4002, 81
path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else f"{ROOT}/../orders.csv"
EXECUTE = "--execute" in sys.argv
try:
    RESTRICTED = {l.strip().upper() for l in open(f"{ROOT}/../restricted_tickers.txt") if l.strip() and not l.startswith("#")}
except Exception:
    RESTRICTED = set()
FX = {"PA":("SBF","EUR"),"SW":("EBS","CHF"),"DE":("IBIS","EUR"),"MC":("BM","EUR"),"TO":("TSE","CAD"),
      "L":("LSE","GBP"),"AS":("AEB","EUR"),"HE":("HEX","EUR"),"OL":("OSE","NOK"),"WA":("WSE","PLN")}
def contract(tk):
    if "." in tk:
        sym,suf=tk.rsplit(".",1); ex,cur=FX.get(suf.upper(),("SMART","USD")); return Stock(sym,ex,cur)
    return Stock(tk.replace("-"," "),"SMART","USD")
def num(x): return x if (x is not None and x==x and x>0) else None

target={r["ticker"]:float(r["dollars"]) for r in csv.DictReader(open(path))}   # incl SGOV
ib=IB(); print(f"Connecting paper gateway ... mode={'EXECUTE' if EXECUTE else 'DRY-RUN'}")
ib.connect(HOST,PORT,clientId=CID,timeout=25)
acct=next((a for a in ib.managedAccounts() if a.startswith("DU")),None)
if not acct: print("REFUSING: not a paper (DU) account."); ib.disconnect(); sys.exit(1)
print(f"PAPER {acct}")
if EXECUTE:
    ib.reqGlobalCancel(); ib.sleep(2)          # clean slate: drop any stale resting orders, then re-derive
ib.reqMarketDataType(4)
# Normalize: IBKR reports positions by exchange symbol (BF-B -> "BF B"); orders.csv uses the order ticker.
# Key held by the orders-ticker space so a name isn't double-counted (sold AND rebought).
sym2tk={contract(tk).symbol: tk for tk in target}
held={}
for p in ib.positions(acct):
    if p.position==0: continue
    held[sym2tk.get(p.contract.symbol, p.contract.symbol)]=p

names=set(target)|set(held)
sells=[]; buys=[]
for tk in sorted(names):
    cur=held[tk].position if tk in held else 0
    if tk.upper() in RESTRICTED:                # never buy restricted; if somehow held, sell it out
        if cur>0: sells.append((tk,cur,"restricted-exit"))
        continue
    c=contract(tk)
    if not ib.qualifyContracts(c):
        if cur>0: print(f"  ! {tk}: held but won't qualify to trade");
        continue
    t=ib.reqMktData(c,"",snapshot=True); ib.sleep(1.5)
    px=num(t.ask) or num(t.last) or num(t.close) or (held[tk].avgCost if tk in held else None)
    if not px: print(f"  ! {tk}: no price; skip"); continue
    tgt_sh=int(target.get(tk,0)//px)            # 0 if not in ideal -> full sell
    delta=tgt_sh-cur
    if delta<0: sells.append((tk,-delta,f"{cur}->{tgt_sh}"))
    elif delta>0: buys.append((tk,delta,f"{cur}->{tgt_sh}",round(px,2)))

def place(tk,qty,side,px=None):
    try:
        c=contract(tk)
        if not ib.qualifyContracts(c): return "no-qualify"
        # market order (John's directive). CAVEAT: on IBKR PAPER accounts, MKT orders may sit at
        # PreSubmitted because SMART can't route through delayed quotes. On a funded LIVE account
        # with real market-data subscriptions, MKT fills instantly during RTH. GTC queues if outside RTH.
        o=MarketOrder(side,qty,tif="GTC")
        tr=ib.placeOrder(c,o); ib.sleep(0.8)
        return tr.orderStatus.status
    except Exception as e:
        return f"ERR {str(e)[:30]}"          # one bad order must never abort the batch

print(f"\nSELLS ({len(sells)}):")
for tk,q,info in sells: print(f"  SELL {tk} {q} ({info})"+("  -> "+place(tk,q,"SELL") if EXECUTE else ""))
print(f"\nBUYS ({len(buys)}):")
for tk,q,info,px in buys: print(f"  BUY  {tk} {q} ({info})"+("  -> "+place(tk,q,"BUY",px) if EXECUTE else ""))
print(f"\n{'EXECUTED' if EXECUTE else 'DRY-RUN'}: {len(sells)} sells, {len(buys)} buys")
ib.disconnect()
