#!/usr/bin/env python3
"""Build per-video wiki pages + machine-readable claim corpus from cleaned transcripts."""
import re, os, glob, json
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__))
TX=f'{ROOT}/transcripts'
VID=f'{ROOT}/wiki/videos'
META=f'{ROOT}/wiki/_meta'
os.makedirs(VID, exist_ok=True); os.makedirs(META, exist_ok=True)

idx={}
for l in open(f'{ROOT}/_video_index.txt'):
    p=l.rstrip('\n').split('|')
    if len(p)>=2: idx[p[0]]={'title':p[1],'duration':p[2] if len(p)>2 else ''}

# --- signal classification (title + content) ---
STRAT_KW=['option','put','call','wheel','covered call','strike','expiration','delta','greek',
 'spread','cash secured','cash geared','portfolio secured','assigned','assignment','premium',
 'theta','roll','margin','collateral','buying power','iron condor','credit spread','dte']
FEAR_KW=['crash','ww3','terrifying','bubble','tom lee','powell','trump','iran','recession','collapse','stimulus']
HYPE_KW=['millionaire','make millions','average joes','never work again','unthinkable','unimaginable','parabolic','skyrocket']

# sentences carrying real method signal: strategy keyword AND/OR a numeric parameter
NUM_PAT=re.compile(r'(\b\d{1,3}\s?%|\b0?\.\d{1,2}\s?delta|\b\d{1,3}\s?(?:day|dte|week|month)s?\b|'
                   r'\$\d[\d,\.]*|\b\d{1,2}\s?(?:to|-)\s?\d{1,2}\s?%|\bstrike\b|\bdelta\b)', re.I)
STRAT_PAT=re.compile('|'.join(re.escape(k) for k in STRAT_KW), re.I)

def split_sents(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]

def classify(title, n_claims):
    """Method-density driven: a video's category/signal reflects how much reproducible
    parameter-bearing strategy content it actually yielded, NOT how often it says 'options'."""
    tl=title.lower()
    fear=sum(tl.count(k) for k in FEAR_KW)
    hype=sum(tl.count(k) for k in HYPE_KW)
    picks=any(k in tl for k in ['stock','etf','nvidia','tesla','ai stock','palantir','amd'])
    if n_claims>=21: return 'STRATEGY',5
    if n_claims>=11: return 'STRATEGY',4
    if n_claims>=6:  return 'STRATEGY',3
    if n_claims>=3:  return 'STRATEGY',2
    if fear>=1:  return 'MACRO', (1 if n_claims else 0)
    if picks and hype: return 'PICKS', (1 if n_claims else 0)
    if hype>=1:  return 'HYPE', (1 if n_claims else 0)
    if picks:    return 'PICKS', (1 if n_claims else 0)
    if n_claims>=1: return 'STRATEGY',1
    return 'OTHER',0

claims=[]; cats={}; pages=0
for f in sorted(glob.glob(f'{TX}/*.txt')):
    vid=os.path.basename(f)[:-4]
    text=open(f).read()
    title=idx.get(vid,{}).get('title','')
    dur=idx.get(vid,{}).get('duration','')
    sents=split_sents(text)
    # extract method-bearing sentences
    method=[s for s in sents if STRAT_PAT.search(s) and (NUM_PAT.search(s) or len(STRAT_PAT.findall(s))>=2)]
    # dedupe near-identical
    seen=set(); keep=[]
    for s in method:
        k=re.sub(r'[^a-z0-9 ]','',s.lower())[:80]
        if k in seen: continue
        seen.add(k); keep.append(s)
    cat,signal=classify(title,len(keep))
    cats[vid]={'title':title,'category':cat,'signal':signal,'words':len(text.split()),'claims':len(keep)}
    for s in keep:
        claims.append({'video':vid,'category':cat,'signal':signal,'claim':s})
    # write page
    fm=f"---\nid: {vid}\ntitle: \"{title.replace(chr(34),chr(39))}\"\ntype: video\ncategory: {cat}\nsignal: {signal}\nduration_sec: {dur}\nwords: {len(text.split())}\nsource: https://www.youtube.com/watch?v={vid}\n---\n\n"
    body=f"# {title}\n\n**Category:** {cat} | **Signal:** {signal}/5 | **Length:** {text.split().__len__()} words\n\n"
    if keep:
        body+="## Method-bearing statements (auto-extracted)\n"+ "\n".join(f"- {s}" for s in keep[:60])+"\n"
    else:
        body+="## Method-bearing statements\n- None — no reproducible strategy content (clickbait/macro/hype).\n"
    open(f'{VID}/{vid}.md','w').write(fm+body)
    pages+=1

json.dump(cats, open(f'{META}/video_categories.json','w'), indent=1)
with open(f'{META}/claims.jsonl','w') as o:
    for c in claims: o.write(json.dumps(c)+'\n')
from collections import Counter
cc=Counter(v['category'] for v in cats.values())
print(f'pages={pages} claims={len(claims)}')
print('categories:', dict(cc))
