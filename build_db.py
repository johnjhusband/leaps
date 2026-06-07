#!/usr/bin/env python3
"""Build leaps.db (SQLite) — the queryable data layer + rebalance history.

Tables:
  companies(ticker PK, name, country, mktcap_B, in_qqq, in_spy, in_russell, in_global, fractional, exchange)
  snapshots(snapshot_date, ticker, golden_verdict, golden_pct, golden_valid, eps_2y, eps_now,
            eps_growth_2y, price_growth_2y, pe_then, pe_now, proxy_verdict, proxy_pct, price,
            intrinsic_value, ttm_eps, fwd_eps, trailing_pe, growth_curr_yr, growth_next_yr,
            growth_ttm_yoy, g_used, moat_proxy_20, gross_margin, oper_margin, roe, debt_to_equity,
            PRIMARY KEY(snapshot_date, ticker))            <- each rebuild APPENDS a dated row
  market_gate(snapshot_date PK, median_golden_pct, breadth_pct, deploy)
  videos(video_id PK, title, category, signal, claims, words)
  claims(id PK, video_id, category, signal, claim)

Usage: python3 build_db.py [YYYY-MM-DD]   (date defaults to argv or env LEAPS_SNAPSHOT_DATE)
"""
import sqlite3, csv, json, os, sys
ROOT='/home/john/repos/leaps'
DATE = (sys.argv[1] if len(sys.argv)>1 else os.environ.get('LEAPS_SNAPSHOT_DATE','')).strip()
if not DATE:
    print('ERROR: pass a snapshot date YYYY-MM-DD (so rebalance history is stamped).'); sys.exit(1)

con=json.load(open(f'{ROOT}/_constituents.json'))
spy,qqq,rus,glb=set(con['SPY']),set(con['QQQ']),set(con.get('RUSSELL1000',[])),set(con.get('GLOBAL1000',[]))
db=sqlite3.connect(f'{ROOT}/leaps.db'); c=db.cursor()

c.executescript('''
CREATE TABLE IF NOT EXISTS companies(ticker TEXT PRIMARY KEY, name TEXT, country TEXT, mktcap_B REAL,
  in_qqq INT, in_spy INT, in_russell INT, in_global INT, fractional INT, exchange TEXT);
CREATE TABLE IF NOT EXISTS snapshots(snapshot_date TEXT, ticker TEXT, golden_verdict TEXT, golden_pct REAL,
  golden_valid TEXT, eps_2y REAL, eps_now REAL, eps_growth_2y REAL, price_growth_2y REAL, pe_then REAL,
  pe_now REAL, proxy_verdict TEXT, proxy_pct REAL, price REAL, intrinsic_value REAL, ttm_eps REAL,
  fwd_eps REAL, trailing_pe REAL, growth_curr_yr REAL, growth_next_yr REAL, growth_ttm_yoy REAL,
  g_used REAL, moat_proxy_20 REAL, gross_margin REAL, oper_margin REAL, roe REAL, debt_to_equity REAL,
  PRIMARY KEY(snapshot_date, ticker));
CREATE TABLE IF NOT EXISTS market_gate(snapshot_date TEXT PRIMARY KEY, median_golden_pct REAL,
  breadth_pct REAL, deploy TEXT);
CREATE TABLE IF NOT EXISTS videos(video_id TEXT PRIMARY KEY, title TEXT, category TEXT, signal INT,
  claims INT, words INT);
CREATE TABLE IF NOT EXISTS claims(id INTEGER PRIMARY KEY, video_id TEXT, category TEXT, signal INT, claim TEXT);
''')

def num(x):
    try: return float(x)
    except: return None

rows=list(csv.DictReader(open(f'{ROOT}/universe_full.csv')))
# companies (current membership — replace)
c.execute('DELETE FROM companies')
for r in rows:
    t=r['ticker']
    c.execute('INSERT OR REPLACE INTO companies VALUES (?,?,?,?,?,?,?,?,?,?)',
      (t, r['name'], r['country'], num(r['mktcap_B']), int(t in qqq), int(t in spy),
       int(t in rus), int(t in glb), 1 if r.get('fractional')=='Y' else 0, r.get('exchange','')))
# snapshot (append for this date; replace this date if re-run)
c.execute('DELETE FROM snapshots WHERE snapshot_date=?', (DATE,))
cols=['golden_verdict','golden_pct','golden_valid','eps_2y','eps_now','eps_growth_2y','price_growth_2y',
      'pe_then','pe_now','proxy_verdict','proxy_pct','price','intrinsic_value','ttm_eps','fwd_eps',
      'trailing_pe','growth_curr_yr','growth_next_yr','growth_ttm_yoy','g_used','moat_proxy_20',
      'gross_margin','oper_margin','roe','debt_to_equity']
for r in rows:
    vals=[DATE, r['ticker']]+[ (r[k] if k.endswith('verdict') or k=='golden_valid' else num(r[k])) for k in cols ]
    c.execute(f"INSERT INTO snapshots VALUES ({','.join('?'*len(vals))})", vals)
# market gate snapshot
mg_path=f'{ROOT}/market_direction.json'
if os.path.exists(mg_path):
    pass  # gate text lives in MARKET_DIRECTION.md; store from goldenline if available
try:
    import goldenline as gl
    g=gl.load_golden()
    gate=gl.market_gate(g, con['SPY'], {t:(num(next((x['mktcap_B'] for x in rows if x['ticker']==t),0)) or 0) for t in con['SPY']})
    if gate:
        c.execute('INSERT OR REPLACE INTO market_gate VALUES (?,?,?,?)',
          (DATE, gate['median_golden_pct'], gate['breadth_pct'], gate['deploy']))
except Exception as e:
    print('  (market gate not stored:', str(e)[:50], ')')

# videos + claims (replace — they don't change across rebalances)
vc=json.load(open(f'{ROOT}/wiki/_meta/video_categories.json'))
c.execute('DELETE FROM videos')
for vid,m in vc.items():
    c.execute('INSERT OR REPLACE INTO videos VALUES (?,?,?,?,?,?)',
      (vid, m.get('title'), m.get('category'), m.get('signal'), m.get('claims',0), m.get('words')))
c.execute('DELETE FROM claims')
for i,line in enumerate(open(f'{ROOT}/wiki/_meta/claims.jsonl')):
    j=json.loads(line)
    c.execute('INSERT INTO claims VALUES (?,?,?,?,?)', (i, j['video'], j['category'], j['signal'], j['claim']))

db.commit()
n_snap=c.execute('SELECT COUNT(DISTINCT snapshot_date) FROM snapshots').fetchone()[0]
print(f'leaps.db built. snapshot date {DATE}. tables: companies={c.execute("SELECT COUNT(*) FROM companies").fetchone()[0]}, '
      f'snapshots rows={c.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]} across {n_snap} date(s), '
      f'videos={c.execute("SELECT COUNT(*) FROM videos").fetchone()[0]}, claims={c.execute("SELECT COUNT(*) FROM claims").fetchone()[0]}')
db.close()
