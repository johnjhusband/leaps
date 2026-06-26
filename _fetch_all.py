import yfinance as yf, json, os, time, _cache
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ'])|set(con.get('RUSSELL1000',[]))|set(con.get('GLOBAL1000',[])))
fp=f'{ROOT}/_fundamentals.json'; gp=f'{ROOT}/_growth.json'
fund=json.load(open(fp)) if os.path.exists(fp) else {}; growth=json.load(open(gp)) if os.path.exists(gp) else {}
MAXAGE=_cache.price_max_age()                                    # price/growth go stale daily; refetch if older
done=0; fail=0
todo=[t for t in tickers if not (_cache.is_fresh(fund.get(t), MAXAGE) and _cache.is_fresh(growth.get(t), MAXAGE))]
print(f'tickers={len(tickers)} need_fetch={len(todo)} (price cache max age {MAXAGE}d)', flush=True)
def pull_fund(tk):
    """Fetch one ticker's fundamentals; returns a dict. Empty (no price) -> retried by fetch_retry."""
    try:
        t=yf.Ticker(tk); info=t.info
        price=info.get('currentPrice') or info.get('regularMarketPrice')
        if not price:
            try: price=t.fast_info.get('lastPrice')
            except: price=None
        return {'price':price,'trailingEps':info.get('trailingEps'),'forwardEps':info.get('forwardEps'),
                'earningsGrowth':info.get('earningsGrowth'),'trailingPE':info.get('trailingPE'),
                'sector':info.get('sector'),'name':info.get('shortName')}
    except Exception as e:
        return {'price':None,'error':str(e)[:80]}
_empty=lambda r: not (isinstance(r,dict) and r.get('price'))   # no price = failed fetch -> retry
for i,tk in enumerate(todo):
    try:
        t=yf.Ticker(tk)
        if not _cache.is_fresh(fund.get(tk), MAXAGE):
            fund[tk]=_cache.stamp(_cache.fetch_retry(lambda: pull_fund(tk), _empty))  # retry transient misses
        if not _cache.is_fresh(growth.get(tk), MAXAGE):
            rec={'have':True,'y0':None,'y1':None,'ltg':None}
            try:
                ge=t.growth_estimates
                if ge is not None and 'stockTrend' in ge.columns:
                    st=ge['stockTrend']
                    def g(k):
                        try:
                            v=st.get(k); return None if v is None or (isinstance(v,float) and v!=v) else float(v)
                        except: return None
                    rec['y0']=g('0y'); rec['y1']=g('+1y'); rec['ltg']=g('LTG')
            except: pass
            growth[tk]=_cache.stamp(rec)
        done+=1
    except Exception as e:
        fund.setdefault(tk,_cache.stamp({'price':None,'error':str(e)[:80]})); fail+=1
    if i%25==0:
        json.dump(fund,open(fp,'w')); json.dump(growth,open(gp,'w'))
        print(f'{i}/{len(todo)} done={done} fail={fail}', flush=True)
    time.sleep(0.3)
json.dump(fund,open(fp,'w')); json.dump(growth,open(gp,'w'))
have=sum(1 for t in tickers if fund.get(t,{}).get('price'))
missing=[t for t in tickers if not fund.get(t,{}).get('price')]   # no price after retries
print(f'COMPLETE priced={have}/{len(tickers)} | NO-DATA after retries: {len(missing)}', flush=True)
if missing:
    print('  DROPPED (no price, excluded from screen):', ', '.join(sorted(missing)[:40]), flush=True)
