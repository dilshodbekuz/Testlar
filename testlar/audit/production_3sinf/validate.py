"""Validate grade-3 integrity and refuse full publication while reviews are incomplete."""
import json,hashlib,sys
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[2];O=R/'audit/production_3sinf'
def digest(q):return hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def approved(q,record):return bool(record and record['status']=='joriy_tekshirildi' and record['sha256']==digest(q))
def main():
 records=json.loads((O/'review_ledger.json').read_text(encoding='utf-8'));lookup={(r['file'],r['question_no']):r for r in records};errors=[];total=0;ready=0;seen=set()
 assert len(lookup)==len(records),'Duplicate review keys'
 for folder in sorted((R/'3-sinf').iterdir()):
  if not folder.is_dir():continue
  ps=sorted(folder.glob('[0-9]*.json'));topics=[];idx=json.loads((folder/'_testlar_index.json').read_text(encoding='utf-8'))
  if {x['fayl'] for x in idx}!={p.name for p in ps}:errors.append('Index file mismatch: '+folder.name)
  if len({x['id'] for x in idx})!=len(idx):errors.append('Duplicate IDs: '+folder.name)
  for p in ps:
   d=json.loads(p.read_text(encoding='utf-8'));topics.append(d)
   for n,q in enumerate(d['savollar'],1):
    key=(p.relative_to(R).as_posix(),n);seen.add(key);rec=lookup.get(key);total+=1
    if not rec or rec['sha256']!=digest(q):errors.append(f'Stale or missing review: {key}')
    if not isinstance(q['savol'],str) or not q['savol'].strip() or len(q['variantlar'])!=4 or type(q['togri'])!=int or not 0<=q['togri']<4:errors.append(f'Invalid question: {key}')
    ready+=approved(q,rec)
  if ps:
   agg=json.loads((folder/'_TOLIQ.json').read_text(encoding='utf-8'))
   if Counter(json.dumps(x,ensure_ascii=False,sort_keys=True) for x in agg)!=Counter(json.dumps(x,ensure_ascii=False,sort_keys=True) for x in topics):errors.append('Aggregate mismatch: '+folder.name)
 if seen!=set(lookup):errors.append('Review ledger inventory mismatch')
 if errors:print(json.dumps(errors,ensure_ascii=False,indent=2));return 1
 print(f'Integrity OK: {total} questions; {ready} currently approved; {total-ready} without current approval.')
 if '--production' in sys.argv:
  status=json.loads((O/'NASHR_HOLATI.json').read_text(encoding='utf-8'))
  if ready!=total or not status.get('production_ready'):
   print('PUBLICATION BLOCKED: '+ '; '.join(status.get('blocking_reasons', ['Incomplete review'])));return 2
 return 0
if __name__=='__main__':raise SystemExit(main())

