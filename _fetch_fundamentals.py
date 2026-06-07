import yfinance as yf, json, os, time, sys
ROOT='/home/john/repos/leaps'
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ']))
cache_path=f'{ROOT}/_fundamentals.json'
cache=json.load(open(cache_path)) if os.path.exists(cache_path) else {}
done=0; fail=0
for i,tk in enumerate(tickers):
    if tk in cache and cache[tk].get('price'): continue
    try:
        t=yf.Ticker(tk)
        info=t.info
        price=info.get('currentPrice') or info.get('regularMarketPrice')
        if not price:
            try: price=t.fast_info.get('lastPrice')
            except: price=None
        cache[tk]={
            'price':price,
            'trailingEps':info.get('trailingEps'),
            'forwardEps':info.get('forwardEps'),
            'earningsGrowth':info.get('earningsGrowth'),
            'trailingPE':info.get('trailingPE'),
            'sector':info.get('sector'),
            'name':info.get('shortName'),
        }
        done+=1
    except Exception as e:
        cache[tk]={'price':None,'error':str(e)[:80]}; fail+=1
    if i%25==0:
        json.dump(cache, open(cache_path,'w'))
        print(f'{i}/{len(tickers)} done={done} fail={fail}', flush=True)
    time.sleep(0.3)
json.dump(cache, open(cache_path,'w'))
print(f'COMPLETE total={len(tickers)} have_price={sum(1 for v in cache.values() if v.get("price"))}', flush=True)
