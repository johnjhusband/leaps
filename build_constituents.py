#!/usr/bin/env python3
"""Step 1 — build the constituent lists for all four baskets into _constituents.json.

Sources (all free, no API key):
  SPY (S&P 500)      : Wikipedia 'List of S&P 500 companies'
  QQQ (Nasdaq-100)   : Wikipedia 'Nasdaq-100'
  RUSSELL1000 proxy  : top 1000 US-listed by market cap from the NASDAQ screener API
  GLOBAL1000         : top 1000 worldwide by market cap from companiesmarketcap.com CSV
"""
import urllib.request, csv, io, json, sys
from io import StringIO
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'}
def get(url, accept='text/html'):
    req=urllib.request.Request(url, headers={**UA,'Accept':accept})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8','ignore')

def spy():
    import pandas as pd
    t=pd.read_html(StringIO(get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')))[0]
    return sorted(set(t['Symbol'].astype(str).str.replace('.','-',regex=False)))

def qqq():
    import pandas as pd
    for t in pd.read_html(StringIO(get('https://en.wikipedia.org/wiki/Nasdaq-100'))):
        for c in t.columns:
            if str(c).lower() in ('ticker','symbol'):
                return sorted(set(t[c].astype(str).str.replace('.','-',regex=False)))
    raise RuntimeError('QQQ table not found')

def russell1000():
    raw=get('https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=5000&download=true',
            accept='application/json, text/plain, */*')
    rows=json.loads(raw)['data']['rows']
    def mc(r):
        v=(r.get('marketCap') or '').replace(',','').replace('$','').strip()
        try: return float(v)
        except: return 0.0
    clean=[]
    for r in rows:
        s=r['symbol'].strip().upper()
        if not s or not all(c.isalnum() or c in '.-' for c in s) or mc(r)<=0: continue
        clean.append((s.replace('.','-'), mc(r)))
    clean.sort(key=lambda x:-x[1]); seen=set(); top=[]
    for s,_ in clean:
        if s in seen: continue
        seen.add(s); top.append(s)
        if len(top)>=1000: break
    return top

def global1000():
    raw=get('https://companiesmarketcap.com/?download=csv', accept='text/csv')
    rows=list(csv.DictReader(io.StringIO(raw)))
    def mc(r):
        try: return float(r['marketcap'])
        except: return 0
    rows=[r for r in rows if mc(r)>0 and r['Symbol'].strip()]
    rows.sort(key=lambda r:-mc(r)); seen=set(); top=[]
    for r in rows:
        s=r['Symbol'].strip()
        if s in seen: continue
        seen.add(s); top.append(s)
        if len(top)>=1000: break
    # also stash the raw rows (name/country/marketcap) for later labeling
    json.dump(rows, open(f'{ROOT}/_global_raw.json','w'))
    return top

con={'SPY':spy(),'QQQ':qqq(),'RUSSELL1000':russell1000(),'GLOBAL1000':global1000()}
json.dump(con, open(f'{ROOT}/_constituents.json','w'), indent=0)
print({k:len(v) for k,v in con.items()})
