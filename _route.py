#!/usr/bin/env python3
"""Route extracted claims to strategy decision-dimensions; emit digests for synthesis."""
import json, re, os, collections
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
claims=[json.loads(l) for l in open(f'{ROOT}/wiki/_meta/claims.jsonl')]
DIM={
 'instrument-selection': r'\b(nasdaq|qqq|s&amp;p|s&p|spy|nvidia|company|companies|ticker|underlying|index|etf|valuation|blue chip|quality|which stock)\b',
 'strike-selection': r'\b(strike|delta|% below|percent below|out of the money|otm|in the money|itm|moneyness|10%|how far)\b',
 'expiration-duration': r'\b(expiration|expir|dte|days to|duration|two[- ]year|2[- ]year|leap|long dated|long-dated|monthly|weekly|45 day|year out|short duration|long duration)\b',
 'entry-timing': r'\b(enter|entry|when to (buy|sell|open)|sell the put|open the|wait for|dip|pullback|timing|chart says|when i sell)\b',
 'exit-profit-taking': r'\b(take profit|close the|buy.?back|exit|50%|when to close|roll up|let it expire|assignment.{0,20}avoid|squeeze)\b',
 'assignment-handling': r'\b(assigned|assignment|get the shares|put to me|take the shares|roll the|roll down|roll out|cost basis)\b',
 'position-sizing-ratios': r'\b(ratio|portfolio secured|cash secured|cash geared|buying power|margin|collateral|% of (my |the )?portfolio|allocat|on the hook|notional|leverage|how many contracts|per contract|in check)\b',
 'market-regime': r'\b(bull market|bare market|bear market|crash|correction|volatility|vix|all market|survives|downturn|recession|sell.?off|drawdown)\b',
}
DIMc={k:re.compile(v,re.I) for k,v in DIM.items()}
routed=collections.defaultdict(list)
for c in claims:
    if c['signal']<2: continue  # only method-bearing
    for dim,pat in DIMc.items():
        if pat.search(c['claim']):
            routed[dim].append(c)
os.makedirs(f'{ROOT}/wiki/_meta/digests',exist_ok=True)
summary={}
for dim,cs in routed.items():
    # dedupe globally by normalized text, keep highest signal, sort by signal desc
    best={}
    for c in cs:
        k=re.sub(r'[^a-z0-9 ]','',c['claim'].lower())[:90]
        if k not in best or c['signal']>best[k]['signal']: best[k]=c
    uniq=sorted(best.values(), key=lambda c:-c['signal'])
    with open(f'{ROOT}/wiki/_meta/digests/{dim}.md','w') as o:
        o.write(f'# Digest: {dim}  ({len(uniq)} unique claims)\n\n')
        for c in uniq:
            o.write(f"- [{c['signal']}] {c['claim']}  ([[{c['video']}]])\n")
    summary[dim]=len(uniq)
json.dump(summary, open(f'{ROOT}/wiki/_meta/digests/_summary.json','w'), indent=1)
print('routed claims to dimensions:')
for k,v in sorted(summary.items(),key=lambda x:-x[1]): print(f'  {k:26} {v}')
