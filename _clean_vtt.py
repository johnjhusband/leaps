#!/usr/bin/env python3
"""Convert raw_transcripts/*.vtt -> clean plain-text transcripts/<id>.txt (deduped)."""
import re, os, glob, json
RAW='/home/john/repos/leaps/raw_transcripts'
OUT='/home/john/repos/leaps/transcripts'
os.makedirs(OUT, exist_ok=True)
idx={}
for l in open('/home/john/repos/leaps/_video_index.txt'):
    p=l.rstrip('\n').split('|')
    if len(p)>=2: idx[p[0]]={'title':p[1],'duration':p[2] if len(p)>2 else ''}

def clean(path):
    lines=[]
    for line in open(path, encoding='utf-8', errors='ignore'):
        line=line.rstrip('\n')
        if '-->' in line or not line.strip(): continue
        if line.startswith(('WEBVTT','Kind:','Language:','NOTE')): continue
        line=re.sub(r'<[^>]+>','',line)
        line=re.sub(r'&nbsp;',' ',line).strip()
        if line and (not lines or lines[-1]!=line): lines.append(line)
    text=re.sub(r'\s+',' ',' '.join(lines)).strip()
    return text

seen={}
for f in sorted(glob.glob(f'{RAW}/*.vtt')):
    vid=os.path.basename(f).split('.')[0]
    # prefer .en.vtt over .en-orig.vtt; keep longest
    txt=clean(f)
    if vid not in seen or len(txt)>len(seen[vid][1]):
        seen[vid]=(f,txt)

manifest=[]
for vid,(f,txt) in seen.items():
    with open(f'{OUT}/{vid}.txt','w') as o: o.write(txt)
    meta=idx.get(vid,{})
    manifest.append({'id':vid,'title':meta.get('title',''),'duration':meta.get('duration',''),'words':len(txt.split())})
manifest.sort(key=lambda x:-x['words'])
json.dump(manifest, open('/home/john/repos/leaps/_meta/transcripts_manifest.json','w'), indent=1)
print(f'cleaned {len(seen)} transcripts; total words {sum(m["words"] for m in manifest):,}')
