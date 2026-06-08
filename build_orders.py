#!/usr/bin/env python3
"""Phase 3 (prep) — turn the buy list + allocation into a concrete order list.

Reads buy_list.csv (the 185 holdings) and MARKET_DIRECTION.md's stock/bond split, and produces the
dollar amount to put into each name + the bond sleeve. This is the dry-run order list; Phase 3 feeds it
to the IBKR API (cashQty = the dollar amount per name). Live execution needs the account; THIS does not.

Usage: python3 build_orders.py [CAPITAL] [equal|mcap]
       CAPITAL default 100000 ; weighting default 'equal' (the index-with-an-edge feel).
"""
import csv, sys, json, os
ROOT=os.path.dirname(os.path.abspath(__file__))
CAPITAL = float(sys.argv[1]) if len(sys.argv)>1 else 100_000.0
WEIGHT  = sys.argv[2] if len(sys.argv)>2 else 'equal'        # 'equal' or 'mcap'
BOND_ETF = 'SGOV'                                            # short-term Treasury sleeve

# stock/bond split: read the pre-moat sizing the build already computed (market_direction.json), else recompute
stock_w=None
mdj=f'{ROOT}/market_direction.json'
# build_universe prints "stock = min(1, undervalued%/50%)"; recompute from buy_list + a stored value if present
buy=list(csv.DictReader(open(f'{ROOT}/buy_list.csv')))
# pull the stock weight from MARKET_DIRECTION.md (the canonical value), fall back to 0.73
import re
try:
    m=re.search(r'(\d+)% stocks', open(f'{ROOT}/MARKET_DIRECTION.md').read())
    stock_w=int(m.group(1))/100 if m else 0.73
except Exception: stock_w=0.73

stock_cap = CAPITAL*stock_w
bond_cap  = CAPITAL-stock_cap
def mcap(r):
    try: return float(r.get('mktcap_B') or 0)
    except: return 0
if WEIGHT=='mcap':
    tot=sum(mcap(r) for r in buy) or 1
    for r in buy: r['_$']=stock_cap*mcap(r)/tot
else:
    per=stock_cap/len(buy)
    for r in buy: r['_$']=per

with open(f'{ROOT}/orders.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['ticker','name','dollars','moat','golden_pct','note'])
    for r in sorted(buy, key=lambda r:-r['_$']):
        w.writerow([r['ticker'], r['name'], round(r['_$'],2), r.get('moat',''), r.get('golden_pct',''), r.get('reason','')])
    w.writerow([BOND_ETF,'iShares 0-3mo Treasury (bond/short-term sleeve)', round(bond_cap,2),'', '','bond sleeve'])

print(f"Capital ${CAPITAL:,.0f} | weighting={WEIGHT} | split {stock_w*100:.0f}% stocks / {(1-stock_w)*100:.0f}% bonds")
print(f"  {len(buy)} stock orders totaling ${stock_cap:,.0f} (~${stock_cap/len(buy):,.0f} each if equal) + ${bond_cap:,.0f} into {BOND_ETF}")
print(f"  -> orders.csv ({len(buy)+1} rows). Feed `dollars` to IBKR API cashQty per ticker.")
