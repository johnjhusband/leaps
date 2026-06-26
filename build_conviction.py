#!/usr/bin/env python3
"""The concentration sleeve — Brandon's "10-20 high-conviction names" layered on the index.

Two-layer architecture (BUY_DECISION.md §E):
  Layer 1 = the index-with-an-edge: the full buy_list.csv (~179 undervalued moat names) — replaces SPY/QQQ.
  Layer 2 = the concentration sleeve: the top N high-conviction names, OVERWEIGHTED, and the targets of the
            put/call overlay (build_puts.py).

"High conviction" here = on the buy list (undervalued + reliable + moat) AND moat=`yes` (durable, not just
pending) AND largest market cap (liquidity/quality/table-pounder — the names Brandon actually concentrates
on: NVDA/MSFT/GOOG/AMZN/META...). Raw golden_pct is shown but NOT the ranker: tiny-base EPS years spike it
to artifacts (MRK ~4600%), which is not conviction. Size among undervalued moat names is the faithful proxy.

Usage: python3 build_conviction.py [N]      # N default 20
"""
import sys, csv, os
ROOT = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20

# names Brandon explicitly named as current buys in the 2026-06 videos (for cross-check labelling only)
HIS_BUYS = {"NVDA", "META", "GOOG", "GOOGL", "MSFT", "AMZN", "ORCL", "MU", "AVGO", "CRM", "HOOD"}
# price-ceiling avoids: have moats + pass our screen, but Brandon refuses on absolute valuation
# (BUY_DECISION.md back-test gap; AMZN graduated to a buy in the 2026-06 videos, so it is NOT excluded).
PRICE_CEILING = {"WM", "PANW", "COST"}
ARTIFACT_GP = 300   # golden_pct above this is a near-zero-base-EPS artifact, not a real conviction signal

rows = list(csv.DictReader(open(f"{ROOT}/buy_list.csv")))
def mc(r):
    try: return float(r.get("mktcap_B") or 0)
    except: return 0
def gp(r):
    try: return float(r.get("golden_pct") or 0)
    except: return 0

sleeve = [r for r in rows if r.get("moat") == "yes"
          and r["ticker"] not in PRICE_CEILING            # Brandon avoids these on price
          and gp(r) <= ARTIFACT_GP]                       # drop EPS-base-artifact golden reads
sleeve.sort(key=mc, reverse=True)
sleeve = sleeve[:N]

print(f"CONCENTRATION SLEEVE — top {len(sleeve)} high-conviction names (of {len(rows)} in the index-with-an-edge)\n")
print(f"{'#':>2}  {'TKR':6}{'name':26}{'mktcap$B':>9}{'golden%':>8}  his-buy")
for i, r in enumerate(sleeve, 1):
    star = "★" if r["ticker"] in HIS_BUYS else ""
    print(f"{i:>2}  {r['ticker']:6}{r['name'][:25]:26}{mc(r):9.0f}{gp(r):8.0f}  {star}")
overlap = sum(1 for r in sleeve if r["ticker"] in HIS_BUYS)
print(f"\n{overlap}/{len(sleeve)} are names Brandon explicitly said he's buying now (★).")
print("Layer 1 (index-with-an-edge) = full buy_list.csv. Layer 2 (this sleeve) = overweight + put/call overlay (build_puts.py).")
