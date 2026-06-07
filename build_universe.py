#!/usr/bin/env python3
"""Step 5 — assemble final universe CSVs from valuation + data + exchange info.

Filters applied, in order:
  1. de-duplicate across SPY/QQQ/Russell1000/Global1000 -> the union
  2. drop NO-DATA names (no price, or no EPS data) -> can't be valued
  3. classify verdict: bullish / bearish / no_earnings (has data, no positive EPS)
  4. mark fractional-tradable at IBKR: US/Canada/Europe listings + exchange-LISTED ADRs;
     drop Asian/Gulf local listings (non-eligible suffixes) and OTC/pink-sheet ADRs.

Outputs:
  universe_full.csv        — every with-data company, verdict + tradable flags (audit)
  universe_fractional.csv  — FINAL: IBKR-fractional-tradable only (the investable universe)
"""
import json, csv
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
con=json.load(open(f'{ROOT}/_constituents.json')); fund=json.load(open(f'{ROOT}/_fundamentals.json'))
val=json.load(open(f'{ROOT}/_valuation_result.json'))
raw={x['Symbol']:x for x in json.load(open(f'{ROOT}/_global_raw.json'))}
try: exch=json.load(open(f'{ROOT}/_exchange.json'))
except FileNotFoundError: exch={}
spy=set(con['SPY']); qqq=set(con['QQQ']); rus=set(con['RUSSELL1000']); glb=set(con['GLOBAL1000'])
union=sorted(spy|qqq|rus|glb)

EU_CA={'TO','V','NE','CN','L','PA','DE','F','SW','AS','BR','MI','MC','MA','ST','HE','CO','OL','LS','VI','IR','WA','PR','AT','SG'}
OTC_CODES={'PNK','OQX','OID','OTC','PINK','OOTC','OTCMKTS',None}   # not IBKR-fractional-eligible

pct={}; flagv={}; vrec={}
for key in ('russell','global','spy','qqq'):
    for side in ('bullish','bearish','neutral'):
        for x in val.get(key,{}).get(side,[]):
            pct.setdefault(x['ticker'], x.get('pct')); flagv.setdefault(x['ticker'], x.get('flag'))
            vrec.setdefault(x['ticker'], x)   # full record: price, g, intrinsic, ...

try: growth=json.load(open(f'{ROOT}/_growth.json'))
except FileNotFoundError: growth={}
try: quality=json.load(open(f'{ROOT}/_quality.json'))
except FileNotFoundError: quality={}
# Brandon's actual valuation method (golden line)
try:
    import goldenline as _gl
    golden=_gl.load_golden()
except Exception:
    golden={}; _gl=None

def fwd_pe(t):
    p=fund.get(t,{}).get('price'); fe=fund.get(t,{}).get('forwardEps')
    return round(p/fe,1) if (p and fe and fe>0) else ''

try:
    import csv as _csv
    MOAT={r['ticker']:r['moat'].strip().lower() for r in _csv.DictReader(open(f'{ROOT}/moat_verdicts.csv'))}
except Exception: MOAT={}

def buy_eligible(t):
    """Brandon's actual screen: golden-bullish AND a reliable read AND not a confirmed no-moat name.
    Reliable = valid (apples-to-apples) OR — when the trailing golden line is SKEWED by a multiple
    re-rating — forward-confirmed: forward P/E justified by growth (PEG-fwd <= 1.5). Quality growers
    like NVDA (skewed but fwd P/E ~16) stay; Tesla (golden-BEARISH) stays out.
    MOAT GATE: a name with a researched verdict of 'no' or 'weak' is removed (cheap-no-moat = value trap,
    e.g. PayPal/Netflix per Brandon). Names not yet researched stay (verdict pending) — see wiki/moats/."""
    if MOAT.get(t) in ('no','weak'): return False          # moat veto
    g=golden.get(t,{})
    if g.get('golden_verdict')!='bullish': return False
    if g.get('golden_valid')=='Y': return True
    fp=fwd_pe(t)                       # skewed -> forward check
    if fp=='' : return False
    grow=(vrec.get(t,{}).get('g') or 0)*100
    return fp <= 1.5*max(grow, 8)

def moat_proxy(t):
    """Approximate Brandon's qualitative Moat (/20) from profitability/quality metrics:
       high margins + high ROE + low debt = pricing power / durable advantage.
       NOT his real moat call — a systematic stand-in. Returns (score_0_20 or '')."""
    q=quality.get(t,{})
    gm,om,roe,de=q.get('gross_margin'),q.get('oper_margin'),q.get('roe'),q.get('debt_to_equity')
    if gm is None and om is None and roe is None: return ''
    s=0
    if gm is not None: s+= 8 if gm>=0.6 else 6 if gm>=0.4 else 4 if gm>=0.25 else 2 if gm>=0.12 else 0
    if om is not None: s+= 6 if om>=0.30 else 4 if om>=0.18 else 2 if om>=0.08 else 0
    if roe is not None: s+= 6 if roe>=0.35 else 5 if roe>=0.20 else 3 if roe>=0.10 else 1 if roe>0 else 0
    if de is not None and de>200: s=max(0,s-2)   # heavy debt erodes durability
    return min(20,s)

def country(t): return raw.get(t,{}).get('country') or ('United States' if (t in spy or t in rus) else 'Unknown')
def mc(t):
    try: return float(raw.get(t,{}).get('marketcap') or 0)
    except: return 0
def has_data(t):
    d=fund.get(t,{})
    return bool(d.get('price')) and d.get('trailingEps') is not None
def verdict(t):
    d=fund.get(t,{})
    if d.get('trailingEps') is not None and d['trailingEps']<=0: return 'no_earnings'
    return flagv.get(t) or ('bullish' if (pct.get(t) or -1)>=0 else 'bearish')
def fractional(t):
    """True if buyable as a fraction at IBKR."""
    if '.' in t:                              # foreign local listing
        return t.rsplit('.',1)[1].upper() in EU_CA
    if country(t)=='United States': return True   # US domestic, exchange-listed
    return exch.get(t) not in OTC_CODES           # ADR: must be exchange-listed, not OTC/pink

withdata=[t for t in union if has_data(t)]
frac=[t for t in withdata if fractional(t)]

def rnd(x, n=2):
    return round(x, n) if isinstance(x,(int,float)) else ''

def write(path, tickers, include_flags):
    """CSV columns explain WHY each rating: the Brandon-valuation inputs are exposed.
    verdict driven by intrinsic vs price; intrinsic = ttm_eps*(1+g)^5*20/1.10^5;
    g = median(growth_curr_yr, growth_next_yr, growth_ttm_yoy), floored 0, capped 0.30."""
    rows=sorted(tickers, key=lambda t:-mc(t))
    with open(path,'w',newline='') as f:
        w=csv.writer(f)
        # golden_* columns first = Brandon's ACTUAL method (primary). proxy columns kept for comparison.
        hdr=['rank','ticker','name','country','mktcap_B','buy',
             'golden_verdict','golden_pct','golden_valid','fwd_pe','eps_2y','eps_now','eps_growth_2y','price_growth_2y','pe_then','pe_now',
             'proxy_verdict','proxy_pct','price','intrinsic_value','ttm_eps','fwd_eps','trailing_pe',
             'growth_curr_yr','growth_next_yr','growth_ttm_yoy','g_used',
             'moat_proxy_20','gross_margin','oper_margin','roe','debt_to_equity']
        if include_flags: hdr+=['fractional','exchange']
        w.writerow(hdr)
        for i,t in enumerate(rows,1):
            nm=(raw.get(t,{}).get('Name') or fund.get(t,{}).get('name') or '')[:40]
            p=pct.get(t); pv=round(p,0) if (p is not None and verdict(t)!='no_earnings') else ''
            d=fund.get(t,{}); gd=growth.get(t,{}); vr=vrec.get(t,{}); q=quality.get(t,{}); gl=golden.get(t,{})
            row=[i,t,nm,country(t),round(mc(t)/1e9,1) if mc(t) else '', 'Y' if buy_eligible(t) else '',
                 gl.get('golden_verdict',''), gl.get('golden_pct',''), gl.get('golden_valid',''), fwd_pe(t),
                 gl.get('eps_2y',''), gl.get('eps_now',''), gl.get('eps_growth_2y',''), gl.get('price_growth_2y',''),
                 gl.get('pe_then',''), gl.get('pe_now',''),
                 verdict(t), pv,
                 rnd(d.get('price')), rnd(vr.get('intrinsic')), rnd(d.get('trailingEps')),
                 rnd(d.get('forwardEps')), rnd(d.get('trailingPE'),1),
                 rnd(gd.get('y0'),3), rnd(gd.get('y1'),3), rnd(d.get('earningsGrowth'),3),
                 rnd(vr.get('g'),3),
                 moat_proxy(t), rnd(q.get('gross_margin'),3), rnd(q.get('oper_margin'),3),
                 rnd(q.get('roe'),3), rnd(q.get('debt_to_equity'),1)]
            if include_flags: row+=['Y' if fractional(t) else 'N', exch.get(t,'') if '.' not in t else t.rsplit('.',1)[1]]
            w.writerow(row)
    return len(rows)

n_full=write(f'{ROOT}/universe_full.csv', withdata, True)
n_frac=write(f'{ROOT}/universe_fractional.csv', frac, False)
from collections import Counter
import statistics
vc=Counter(verdict(t) for t in frac)
print(f'union={len(union)}  with_data={n_full}  fractional_tradable={n_frac}')
print(f'  fractional verdicts: bullish={vc["bullish"]} bearish={vc["bearish"]} no_earnings={vc["no_earnings"]}')
print(f'  fractional country mix non-US: {100*sum(1 for t in frac if country(t)!="United States")/n_frac:.0f}%')

# --- MARKET DIRECTION (macro/deploy gauge) ---
def market_read(splits, label):
    names=[x for x in splits['bullish']+splits['bearish'] if x.get('flag') is None and x.get('pct') is not None]
    pcts=[x['pct'] for x in names]
    wsum=sum(mc(x['ticker']) for x in names) or 1
    cw=sum(x['pct']*mc(x['ticker']) for x in names)/wsum
    breadth=100*sum(1 for p in pcts if p>=0)/len(pcts)
    return {'index':label,'median_under_over_pct':round(statistics.median(pcts)),
            'capwtd_under_over_pct':round(cw),'pct_undervalued_breadth':round(breadth)}
md=[market_read(val['spy'],'SPY'),market_read(val['qqq'],'QQQ'),market_read(val['global'],'Global1000')]
json.dump({'as_of_note':'higher = cheaper market = more bullish to deploy; track trend across rebalances',
           'reads':md}, open(f'{ROOT}/market_direction.json','w'), indent=1)
with open(f'{ROOT}/MARKET_DIRECTION.md','w') as f:
    f.write('# Market Direction — Deploy Gauge\n\n')
    f.write('Brandon deploys aggressively only when the overall market is favorable (his bull-bear scale / '
            'economic scorecard). This is our computable version: where each index sits vs intrinsic value.\n\n')
    f.write('| Index | Median under/over | Cap-weighted under/over | Breadth (% undervalued) |\n')
    f.write('|-------|------------------:|------------------------:|------------------------:|\n')
    for r in md:
        f.write(f"| {r['index']} | {r['median_under_over_pct']:+d}% | {r['capwtd_under_over_pct']:+d}% | {r['pct_undervalued_breadth']}% |\n")
    f.write('\n**Read it as:** higher numbers = cheaper market = more bullish to deploy. The absolute level is '
            'model-tilted, so the real signal is the **trend across rebalances** — if breadth and medians fall '
            'month over month, the market is getting expensive (be selective); if they rise, deploy more.\n')
    # Brandon's actual >20% market gate (golden line on S&P names)
    gate=_gl.market_gate(golden, con['SPY'], {t:mc(t) for t in con['SPY']}) if _gl and golden else None
    if gate:
        f.write(f"\n## Deploy gate (golden line on the S&P — Brandon's >20% rule)\n")
        f.write(f"- Median golden-line read across {gate['valid_names']} valid S&P names: "
                f"**{gate['median_golden_pct']:+d}%** (breadth {gate['breadth_pct']}% undervalued).\n")
        f.write(f"- **{gate['deploy']}.** (Gate trips when the market is >20% overvalued, i.e. price ran "
                f">20% ahead of earnings. Uses apples-to-apples valid names only — skewed mega-caps excluded.)\n")
    # Capital allocation (INDEX_PLAN.md): 50% of universe undervalued = 100% stocks.
    fr=[t for t in frac]
    valued_n=sum(1 for t in fr if golden.get(t,{}).get('golden_verdict'))
    buy_n=sum(1 for t in fr if buy_eligible(t))
    if valued_n:
        uv=buy_n/valued_n
        stock=min(1.0, uv/0.50)
        f.write(f"\n## Capital allocation (stocks vs bonds)\n")
        f.write(f"- Genuinely undervalued: **{buy_n}/{valued_n} = {uv*100:.0f}%** of the valued tradable universe.\n")
        f.write(f"- Rule `stock = min(100%, undervalued% ÷ 50%)` -> **{stock*100:.0f}% stocks (the {buy_n} buy-list "
                f"names) / {(1-stock)*100:.0f}% bonds-short-term.**\n")
        print(f'  ALLOCATION: {uv*100:.0f}% undervalued -> {stock*100:.0f}% stocks / {(1-stock)*100:.0f}% bonds')
# buy_list.csv = the fractional, buy-eligible names (valid OR forward-confirmed skewed)
buy=sorted([t for t in frac if buy_eligible(t)], key=lambda t:-mc(t))
with open(f'{ROOT}/buy_list.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['rank','ticker','name','country','mktcap_B','golden_pct','golden_valid','fwd_pe','reason'])
    for i,t in enumerate(buy,1):
        gl=golden.get(t,{}); reason='valid' if gl.get('golden_valid')=='Y' else 'fwd-confirmed'
        w.writerow([i,t,(raw.get(t,{}).get('Name') or fund.get(t,{}).get('name') or '')[:40],country(t),
                    round(mc(t)/1e9,1) if mc(t) else '', gl.get('golden_pct',''), gl.get('golden_valid',''), fwd_pe(t), reason])
print(f'  buy_list.csv: {len(buy)} names ('
      f"{sum(1 for t in buy if golden.get(t,{}).get('golden_valid')=='Y')} valid + "
      f"{sum(1 for t in buy if golden.get(t,{}).get('golden_valid')=='skewed')} fwd-confirmed)")
print(f'  market direction: SPY median {md[0]["median_under_over_pct"]:+d}% breadth {md[0]["pct_undervalued_breadth"]}%  -> MARKET_DIRECTION.md')
if _gl and golden:
    g2=_gl.market_gate(golden, con['SPY'], {t:mc(t) for t in con['SPY']})
    if g2: print(f'  GOLDEN gate (valid median): {g2["median_golden_pct"]:+d}% -> {g2["deploy"]}')
