import yfinance as yf, json, os, time
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
con=json.load(open(f'{ROOT}/_constituents.json'))
tickers=sorted(set(con['SPY'])|set(con['QQQ'])|set(con.get('RUSSELL1000',[]))|set(con.get('GLOBAL1000',[])))
fp=f'{ROOT}/_fundamentals.json'; gp=f'{ROOT}/_growth.json'
fund=json.load(open(fp)) if os.path.exists(fp) else {}; growth=json.load(open(gp)) if os.path.exists(gp) else {}
done=0; fail=0; todo=[t for t in tickers if not (fund.get(t,{}).get('price') and growth.get(t,{}).get('have'))]
print(f'tickers={len(tickers)} need_fetch={len(todo)}', flush=True)
for i,tk in enumerate(todo):
    try:
        t=yf.Ticker(tk)
        if not fund.get(tk,{}).get('price'):
            info=t.info
            price=info.get('currentPrice') or info.get('regularMarketPrice')
            if not price:
                try: price=t.fast_info.get('lastPrice')
                except: price=None
            fund[tk]={'price':price,'trailingEps':info.get('trailingEps'),'forwardEps':info.get('forwardEps'),
                      'earningsGrowth':info.get('earningsGrowth'),'trailingPE':info.get('trailingPE'),
                      'sector':info.get('sector'),'name':info.get('shortName')}
        if not growth.get(tk,{}).get('have'):
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
            growth[tk]=rec
        done+=1
    except Exception as e:
        fund.setdefault(tk,{'price':None,'error':str(e)[:80]}); fail+=1
    if i%25==0:
        json.dump(fund,open(fp,'w')); json.dump(growth,open(gp,'w'))
        print(f'{i}/{len(todo)} done={done} fail={fail}', flush=True)
    time.sleep(0.3)
json.dump(fund,open(fp,'w')); json.dump(growth,open(gp,'w'))
have=sum(1 for t in tickers if fund.get(t,{}).get('price'))
print(f'COMPLETE priced={have}/{len(tickers)}', flush=True)
