import yfinance as yf, json, os, time, _cache
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ'])|set(con.get('RUSSELL1000',[]))|set(con.get('GLOBAL1000',[])))
path=f'{ROOT}/_goldenline.json'
cache=json.load(open(path)) if os.path.exists(path) else {}
MAXAGE=_cache.price_max_age()                                    # prices go stale daily; refetch if older
todo=[t for t in tickers if not _cache.is_fresh(cache.get(t), MAXAGE)]
print(f'goldenline fetch: {len(todo)} of {len(tickers)} (price cache max age {MAXAGE}d)', flush=True)
def pull(tk):
    """One full fetch for a ticker; returns a rec. Empty (no price) -> retried by fetch_retry."""
    rec={}
    try:
        t=yf.Ticker(tk)
        fin=t.income_stmt
        eps=None
        for row in ('Diluted EPS','Basic EPS'):
            if fin is not None and row in fin.index:
                vals=[float(v) if v==v else None for v in fin.loc[row].values]  # NaN->None
                eps=vals; break
        rec['eps_series']=eps  # [FY0, FY-1, FY-2, FY-3] newest first
        h=t.history(period='3y', interval='1mo')
        cl=list(h['Close'].values) if h is not None and len(h) else []
        rec['price_now']=round(float(cl[-1]),2) if cl else None
        rec['price_2y']=round(float(cl[-25]),2) if len(cl)>=25 else (round(float(cl[0]),2) if cl else None)
    except Exception as e:
        rec['err']=str(e)[:50]
    return rec
_empty=lambda r: not (isinstance(r,dict) and r.get('price_now'))   # no price = failed fetch -> retry
for i,tk in enumerate(todo):
    rec=_cache.fetch_retry(lambda: pull(tk), _empty)            # retry transient misses, don't drop silently
    cache[tk]=_cache.stamp(rec)                                  # record fetch date for freshness
    if i%25==0:
        json.dump(cache,open(path,'w')); print(f'{i}/{len(todo)}',flush=True)
    time.sleep(0.2)
json.dump(cache,open(path,'w'))
missing=[t for t in tickers if _empty(cache.get(t))]            # names with NO usable price after retries
print(f'COMPLETE {len(cache)} | NO-DATA after retries: {len(missing)}', flush=True)
if missing:
    print('  DROPPED (no price, excluded from screen):', ', '.join(sorted(missing)[:40]), flush=True)
