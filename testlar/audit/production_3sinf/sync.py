"""Synchronize grade 3 representations; never replace the original textbook contents list."""
import json,shutil,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[2];O=R/'audit/production_3sinf';events=[]
def write(p,text):
 if p.exists() and p.read_text(encoding='utf-8')==text:return
 if p.exists():
  b=O/'backup'/p.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
 p.write_text(text,encoding='utf-8');events.append(p.relative_to(R).as_posix())
def txt(d):
 out=[d['mavzu'],''];last=None
 for i,q in enumerate(d['savollar'],1):
  if q['qiyinlik']!=last:
   last=q['qiyinlik'];out+=['--- '+last.upper()+' ---','']
  out.append(f"{i}. {q['savol']}")
  out.extend(('+' if j==q['togri'] else '')+'ABCD'[j]+') '+v for j,v in enumerate(q['variantlar']))
  out.append('')
 return '\n'.join(out).rstrip()+'\n'
for folder in sorted((R/'3-sinf').iterdir()):
 if not folder.is_dir():continue
 topics=[];index=[]
 for p in sorted(folder.glob('[0-9]*.json')):
  d=json.loads(p.read_text(encoding='utf-8'));topics.append(d)
  write(p.with_suffix('.txt'),txt(d))
  index.append({'id':hashlib.sha256(p.relative_to(R).as_posix().encode()).hexdigest()[:20], 'fayl':p.name,'mavzu':d['mavzu'],'savollar_soni':len(d['savollar'])})
 if topics:write(folder/'_TOLIQ.json',json.dumps(topics,ensure_ascii=False,indent=2)+'\n')
 write(folder/'_testlar_index.json',json.dumps(index,ensure_ascii=False,indent=2)+'\n')
(O/'sync_changes.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Synced files',len(events))
