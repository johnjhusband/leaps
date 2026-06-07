#!/usr/bin/env python3
"""Regression harness: reconcile our screen's buy decision against Brandon's actual stated stock calls
(extracted from the transcripts). Run after any logic change; watch the agree-count climb.
See BACKTEST_RECONCILIATION.md for the analysis. Brandon's call lists below are the ground truth."""
import csv
rows={r['ticker']:r for r in csv.DictReader(open('universe_fractional.csv'))}
# Brandon's stated calls from the transcripts (consolidated across agents)
bull = ['NVDA','META','TSM','HOOD','MRVL','NOW','UNH','MU','GOOGL','GOOG','BAC','MSFT']
bear = ['WM','WMT','SBUX','PYPL','HIMS','PANW','AVGO','NFLX','ASML','SOFI','AAPL','AMZN','TSLA','XOM','CVX','V','NKE','COST','CRM','INTC','AMD']
def ours(tk):
    r=rows.get(tk)
    if not r: return 'NOT-IN-UNIVERSE',''
    return ('BUY' if r['buy']=='Y' else 'no'), f"golden={r['golden_verdict']}/{r['golden_valid']} fwd_pe={r['fwd_pe']} gpct={r['golden_pct']}"
print("=== BRANDON BULLISH — does our screen also BUY? ===")
agree=dis=0
for tk in bull:
    o,info=ours(tk); ok = (o=='BUY'); agree+=ok; dis+= (o=='no')
    print(f"  {tk:6} Brandon=BULL  ours={o:16} {'OK' if ok else ('<-- MISMATCH' if o=='no' else '')}  {info}")
print("\n=== BRANDON BEARISH/AVOID — does our screen correctly NOT buy? ===")
for tk in bear:
    o,info=ours(tk); ok=(o!='BUY')
    print(f"  {tk:6} Brandon=BEAR  ours={o:16} {'OK' if ok else '<-- MISMATCH (we buy, he avoids)'}  {info}")
