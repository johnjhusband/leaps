import yfinance as yf, json, os, time
ROOT='/home/john/repos/leaps'
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ']))
path=f'{ROOT}/_growth.json'
cache=json.load(open(path)) if os.path.exists(path) else {}
done=0;fail=0
for i,tk in enumerate(tickers):
    if tk in cache and cache[tk].get('have'): continue
    rec={'have':True,'y0':None,'y1':None,'ltg':None}
    try:
        ge=yf.Ticker(tk).growth_estimates
        if ge is not None and 'stockTrend' in ge.columns:
            st=ge['stockTrend']
            def g(k):
                try:
                    v=st.get(k)
                    return None if v is None or (isinstance(v,float) and v!=v) else float(v)
                except: return None
            rec['y0']=g('0y'); rec['y1']=g('+1y'); rec['ltg']=g('LTG')
        done+=1
    except Exception as e:
        rec['err']=str(e)[:60]; fail+=1
    cache[tk]=rec
    if i%25==0:
        json.dump(cache,open(path,'w')); print(f'{i}/{len(tickers)} done={done} fail={fail}',flush=True)
    time.sleep(0.3)
json.dump(cache,open(path,'w'))
print(f'COMPLETE total={len(tickers)} have_y0={sum(1 for v in cache.values() if v.get("y0") is not None)}',flush=True)
