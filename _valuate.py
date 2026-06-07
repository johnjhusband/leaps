#!/usr/bin/env python3
"""Apply Brandon's valuation rules to every SPY & QQQ holding; split into bullish/bearish halves.

Brandon's method (reconstructed, applied uniformly — see wiki/strategy/valuation-method.md):
  intrinsic = TTM_EPS * (1+g)^5 * FAIR_PE / (1+DISCOUNT)^5
  g  = conservative 5-yr growth = min(max(g_raw*HAIRCUT, 0), GCAP)
       g_raw = forwardEps/trailingEps-1 if both>0, else earningsGrowth, else 0.08
  ratio = intrinsic/price ; undervalued if ratio>1 (price below intrinsic).
Ranking into halves is by % under/over (rank-based), so FAIR_PE/DISCOUNT (same for all) don't
change WHICH half a stock lands in — they only scale the reported %.
Companies with no positive TTM earnings can't be valued this way -> forced to the bearish (overvalued)
side, flagged 'no_earnings', per Brandon's rule 'if you can't value it conservatively, skip it'.
"""
import json, math
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
FAIR_PE=20.0; DISCOUNT=0.10; HAIRCUT=0.6; GCAP=0.30
con=json.load(open(f'{ROOT}/_constituents.json'))
fund=json.load(open(f'{ROOT}/_fundamentals.json'))
import os
growth=json.load(open(f'{ROOT}/_growth.json')) if os.path.exists(f'{ROOT}/_growth.json') else {}

def valuate(tk):
    d=fund.get(tk,{})
    price=d.get('price'); eps=d.get('trailingEps'); feps=d.get('forwardEps'); eg=d.get('earningsGrowth')
    if not price: return None
    rec={'ticker':tk,'name':d.get('name'),'sector':d.get('sector'),'price':round(price,2),
         'ttm_eps':eps,'fwd_eps':feps,'trailingPE':d.get('trailingPE')}
    if eps is None or eps<=0:
        rec.update({'intrinsic':None,'pct':-999,'g':None,'flag':'no_earnings','verdict':'bearish'})
        return rec
    # Conservative 5-yr growth = median of available forward/actual growth signals.
    # (Earlier bug: using only forwardEPS/trailingEPS captured just NEXT year's modest
    #  analyst bump, understating multi-year compounders like GOOGL -> wrongly bearish.)
    gd=growth.get(tk,{})
    signals=[s for s in (gd.get('y0'), gd.get('y1'), eg) if s is not None]
    if signals:
        signals=sorted(signals); n=len(signals)
        g_raw=signals[n//2] if n%2 else (signals[n//2-1]+signals[n//2])/2
    elif feps and feps>0 and eps>0: g_raw=feps/eps-1   # last-resort fallback
    else: g_raw=0.08
    g=min(max(g_raw,0.0),GCAP)   # cap at GCAP = Brandon's conservatism; floor at 0
    intrinsic=eps*((1+g)**5)*FAIR_PE/((1+DISCOUNT)**5)
    pct=(intrinsic/price-1)*100
    rec.update({'intrinsic':round(intrinsic,2),'pct':round(pct,1),'g':round(g,3),
                'flag':None,'verdict':'bullish' if pct>=0 else 'bearish'})
    return rec

# IBKR fractional eligibility by exchange suffix: US (no suffix) + Canada + Europe = eligible;
# Asia/Mideast/LatAm/Australia local listings = NOT fractional-eligible at IBKR.
EU_CA_SUFFIX={'TO','V','NE','CN',           # Canada
 'L','PA','DE','F','SW','AS','BR','MI','MC','MA','ST','HE','CO','OL','LS','VI','IR','WA','PR','AT','SG'} # Europe
def ibkr_fractional(tk):
    if '-' in tk and tk.rsplit('-',1)[1] in ('A','B'): tk=tk  # US class shares keep
    if '.' not in tk: return True            # US listing
    suf=tk.rsplit('.',1)[1].upper()
    return suf in EU_CA_SUFFIX

def rank_split(tickers, n_each, label):
    vals=[v for v in (valuate(t) for t in tickers) if v]
    for v in vals: v['ibkr_frac']=ibkr_fractional(v['ticker'])
    vals.sort(key=lambda r:-r['pct'])  # most undervalued first
    bullish=vals[:n_each]
    bearish=vals[-n_each:]
    neutral=vals[n_each:len(vals)-n_each] if len(vals)>2*n_each else []
    return {'label':label,'total_valued':len(vals),'n_each':n_each,
            'bullish':bullish,'bearish':bearish,'neutral':neutral}

spy=rank_split(con['SPY'],250,'SPY (S&P 500)')
qqq=rank_split(con['QQQ'],50,'QQQ (Nasdaq-100)')
rus=rank_split(con['RUSSELL1000'],500,'Russell 1000 (top ~1000 US by market cap)')
out={'spy':spy,'qqq':qqq,'russell':rus,'params':{'FAIR_PE':FAIR_PE,'DISCOUNT':DISCOUNT,'GCAP':GCAP}}
allsplits=[spy,qqq,rus]
keymap={'SPY':'SPY','Nasdaq':'QQQ','Russell':'RUSSELL1000','Global':'GLOBAL1000'}
if con.get('GLOBAL1000'):
    # global basket: value all available, then split the VALUED universe in half (some foreign
    # listings lack EPS/growth on yfinance and are skipped, so n_each = floor(valued/2)).
    gvals=[v for v in (valuate(t) for t in con['GLOBAL1000']) if v]
    glb=rank_split(con['GLOBAL1000'], len(gvals)//2, 'Global (top ~1000 companies worldwide by market cap)')
    out['global']=glb; allsplits.append(glb)
json.dump(out, open(f'{ROOT}/_valuation_result.json','w'), indent=1)
for r in allsplits:
    ck=next(v for k,v in keymap.items() if k in r['label'])
    miss=len([t for t in con[ck] if not fund.get(t,{}).get('price')])
    print(f"{r['label']}: valued {r['total_valued']}, {r['n_each']} bullish / {r['n_each']} bearish, "
          f"{len(r['neutral'])} neutral, {miss} unpriced/skipped")
