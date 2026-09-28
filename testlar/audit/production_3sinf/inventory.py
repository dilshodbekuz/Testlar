import json,hashlib
from pathlib import Path
from collections import Counter
R=Path.cwd();reviews=json.loads((R/'audit/manual_reviews.json').read_text(encoding='utf-8'));current={};stats=Counter();changed=[]
for p in (R/'3-sinf').glob('*/*.json'):
 if p.name.startswith('_'):continue
 d=json.loads(p.read_text(encoding='utf-8'))
 for n,q in enumerate(d['savollar'],1):current[(p.relative_to(R).as_posix(),n)]=q
for r in reviews:
 key=(r['file'].replace('\\','/'),r['question_no'])
 if not key[0].startswith('3-sinf/'):continue
 q=current.get(key)
 if q is None:stats['missing']+=1;continue
 h=hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
 if h==r['sha256']:stats['same_'+r['status']]+=1
 else:
  stats['changed_'+r['status']]+=1
  changed.append({'file':key[0],'n':key[1],'old_status':r['status'],'notes':r.get('notes'),'q':q})
print(stats)
(R/'audit/production_3sinf/old_review_changes.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
for f in sorted((R/'3-sinf').iterdir()):
 if not f.is_dir():continue
 ps=[p for p in f.glob('*.json') if not p.name.startswith('_')]
 m=json.loads((f/'_mavzular.json').read_text(encoding='utf-8')) if (f/'_mavzular.json').exists() else []
 print(f.name,len(ps),sum(len(json.loads(p.read_text(encoding='utf-8'))['savollar']) for p in ps),'mavzular',len(m))
print('MATH CHANGED',sum('Matematika/' in x['file'] for x in changed))
