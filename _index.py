#!/usr/bin/env python3
import json, os, glob, re
ROOT='/home/john/repos/leaps'
cats=json.load(open(f'{ROOT}/wiki/_meta/video_categories.json'))
claims=[json.loads(l) for l in open(f'{ROOT}/wiki/_meta/claims.jsonl')]
from collections import Counter
catc=Counter(v['category'] for v in cats.values())
sigc=Counter(v['signal'] for v in cats.values())
index={
 'generated':'2026-06-07',
 'videos_total':len(cats),
 'claims_total':len(claims),
 'categories':dict(catc),
 'signal_distribution':{str(k):sigc[k] for k in sorted(sigc)},
 'layers':{
   'L1_spec':'wiki/strategy/STRATEGY_SPEC.md',
   'L2_decisions':[os.path.basename(p) for p in sorted(glob.glob(f'{ROOT}/wiki/strategy/*.md')) if 'STRATEGY_SPEC' not in p],
   'L3_videos_dir':'wiki/videos/',
   'L4_contradictions':'wiki/strategy/contradictions.md',
   'L5_meta':['_meta/claims.jsonl','_meta/video_categories.json','_meta/digests/'],
 },
 'top_strategy_videos':[{'id':k,'title':v['title'],'claims':v.get('claims',0),'signal':v['signal']}
    for k,v in sorted(cats.items(), key=lambda x:-x[1].get('claims',0))[:25]],
}
json.dump(index, open(f'{ROOT}/wiki/_meta/index.json','w'), indent=1)
print('index written')
# --- VERIFICATION ---
vids=set(cats)
pages=set(os.path.basename(p)[:-3] for p in glob.glob(f'{ROOT}/wiki/videos/*.md'))
missing=vids-pages
print('video pages:', len(pages), '| videos:', len(vids), '| missing pages:', len(missing))
# check every [[id]] citation in strategy/*.md resolves to a real video id
bad=set()
for f in glob.glob(f'{ROOT}/wiki/strategy/*.md'):
    for m in re.findall(r'\[\[([A-Za-z0-9_\-]{6,15})\]\]', open(f).read()):
        if m not in vids and not m.replace('-','').isalpha():
            if m not in ('strategy-spec','instrument-selection','strike-selection','expiration-duration',
                'entry-timing','exit-profit-taking','assignment-handling','position-sizing-ratios',
                'market-regime','contradictions'):
                bad.add(m)
print('unresolved video citations:', len(bad), sorted(bad)[:10])
