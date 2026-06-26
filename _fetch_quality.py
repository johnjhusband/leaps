import yfinance as yf, json, os, time, _cache
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ'])|set(con.get('RUSSELL1000',[]))|set(con.get('GLOBAL1000',[])))
path=f'{ROOT}/_quality.json'
cache=json.load(open(path)) if os.path.exists(path) else {}
MAXAGE=_cache.quality_max_age()                                 # margins/ROE/debt move ~quarterly
todo=[t for t in tickers if not _cache.is_fresh(cache.get(t), MAXAGE)]
print(f'quality fetch: {len(todo)} to fetch of {len(tickers)} (quality cache max age {MAXAGE}d)', flush=True)
for i,t in enumerate(todo):
    try:
        info=yf.Ticker(t).info
        cache[t]=_cache.stamp({'gross_margin':info.get('grossMargins'),'oper_margin':info.get('operatingMargins'),
                  'profit_margin':info.get('profitMargins'),'roe':info.get('returnOnEquity'),
                  'debt_to_equity':info.get('debtToEquity')})
    except Exception as e:
        cache[t]=_cache.stamp({'err':str(e)[:50]})
    if i%25==0:
        json.dump(cache,open(path,'w')); print(f'{i}/{len(todo)}',flush=True)
    time.sleep(0.25)
json.dump(cache,open(path,'w'))
print('COMPLETE', len(cache), flush=True)
