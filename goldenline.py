#!/usr/bin/env python3
"""Brandon's actual valuation method — the "golden line".

Over a ~2-year window: compare how much EPS grew vs how much the stock price grew.
If EPS outgrew price, the stock is undervalued (price lagged earnings) and should revert up.

  eps_growth   = eps_now / eps_2y - 1
  price_growth = price_now / price_2y - 1
  fair_price   = price_2y * (1 + eps_growth)         # where price "should" be on the EPS line
  golden_pct   = fair_price / price_now - 1           # + = undervalued
  validity     = start P/E vs end P/E must be similar (apples-to-apples); if the multiple
                 re-rated a lot the line is "skewed" and the read is unreliable.

Exposes load_golden() -> {ticker: {...}} and market_gate(spy_tickers) for the >20% deploy gate.
"""
import json, statistics
ROOT='/home/john/repos/leaps'

def _eps_pair(series):
    """eps_now = most recent FY; eps_2y = 2 fiscal years earlier (fall back to oldest available)."""
    if not series: return None, None
    s=[v for v in series]                      # newest first
    now=s[0] if len(s)>=1 else None
    two=s[2] if len(s)>=3 and s[2] is not None else (s[-1] if len(s)>1 else None)
    return now, two

def compute(rec):
    en, e2 = _eps_pair(rec.get('eps_series'))
    pn, p2 = rec.get('price_now'), rec.get('price_2y')
    if not (en and e2 and pn and p2) or e2<=0 or en<=0 or p2<=0:
        return None
    eps_g = en/e2 - 1
    price_g = pn/p2 - 1
    fair = p2*(1+eps_g)
    golden_pct = (fair/pn - 1)*100
    pe_then, pe_now = p2/e2, pn/en
    pe_change = pe_now/pe_then - 1
    valid = abs(pe_change) <= 0.5              # within 50% = apples-to-apples
    return {'golden_pct':round(golden_pct), 'eps_now':round(en,2), 'eps_2y':round(e2,2),
            'eps_growth_2y':round(eps_g,2), 'price_growth_2y':round(price_g,2),
            'pe_then':round(pe_then,1), 'pe_now':round(pe_now,1), 'golden_valid':'Y' if valid else 'skewed',
            'golden_verdict':'bullish' if golden_pct>=0 else 'bearish'}

def load_golden():
    raw=json.load(open(f'{ROOT}/_goldenline.json'))
    out={}
    for tk,rec in raw.items():
        c=compute(rec)
        if c: out[tk]=c
    return out

def market_gate(golden, spy_tickers, raw_mc):
    """Market deploy gate on the golden line. Uses MEDIAN of apples-to-apples (valid) S&P names only —
    cap-weighting + skewed mega-caps (NVDA EPS +300%, TSLA PE re-rated) badly distort the read.
    Median < -20% => market >20% overvalued => don't deploy (Brandon's rule)."""
    valid=[t for t in spy_tickers if t in golden and golden[t]['golden_valid']=='Y']
    if not valid: return None
    med=statistics.median(golden[t]['golden_pct'] for t in valid)
    breadth=100*sum(1 for t in valid if golden[t]['golden_pct']>=0)/len(valid)
    overvalued = med < -20
    return {'median_golden_pct':round(med),'breadth_pct':round(breadth),'valid_names':len(valid),
            'market_over_20pct_overvalued':overvalued,
            'deploy':'NO — market >20% overvalued, sit in bonds' if overvalued else 'OK to deploy (market roughly fair)'}

if __name__=='__main__':
    g=load_golden(); print('golden computed for', len(g), 'tickers')
    for tk in ('MSFT','NVDA','GOOG','AAPL','KO'):
        if tk in g: print(tk, g[tk])
