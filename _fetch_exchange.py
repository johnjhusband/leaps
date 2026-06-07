import yfinance as yf, json, os, time
ROOT='/home/john/repos/leaps'
con=json.load(open(f'{ROOT}/_constituents.json')); fund=json.load(open(f'{ROOT}/_fundamentals.json'))
raw={x['Symbol']:x for x in json.load(open(f'{ROOT}/_global_raw.json'))}
cu=json.load(open(f'{ROOT}/_clean_universe.json')); keep=set(cu['keep'])
spy=set(con['SPY']);rus=set(con['RUSSELL1000'])
EU_CA={'TO','V','NE','CN','L','PA','DE','F','SW','AS','BR','MI','MC','MA','ST','HE','CO','OL','LS','VI','IR','WA','PR','AT','SG'}
def trad(t): return ('.' not in t) or (t.rsplit('.',1)[1].upper() in EU_CA)
def ctry(t): return raw.get(t,{}).get('country') or ('United States' if (t in spy or t in rus) else 'Unknown')
adr=[t for t in keep if trad(t) and '.' not in t and ctry(t) not in ('United States','Unknown')]
path=f'{ROOT}/_exchange.json'
cache=json.load(open(path)) if os.path.exists(path) else {}
for i,t in enumerate(adr):
    if t in cache: continue
    try:
        ex=yf.Ticker(t).info.get('exchange')
        cache[t]=ex
    except Exception as e:
        cache[t]=None
    if i%25==0:
        json.dump(cache,open(path,'w')); print(f'{i}/{len(adr)}',flush=True)
    time.sleep(0.25)
json.dump(cache,open(path,'w'))
from collections import Counter
print('COMPLETE', len(cache), 'exchanges:', dict(Counter(cache.values())))
