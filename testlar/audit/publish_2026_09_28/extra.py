import json,re
from pathlib import Path
from collections import defaultdict,Counter
R=Path.cwd(); O=R/'audit/publish_2026_09_28'
groups=defaultdict(list); samples={}; dist={}; manifests=[]
for g in sorted(R.glob('*-sinf')):
 rows=[]; counts=Counter()
 for p in sorted(g.glob('*/*[0-9]*.json')):
  if p.name.startswith('_'):continue
  d=json.loads(p.read_text(encoding='utf-8'))
  for i,q in enumerate(d.get('savollar',[]),1):
   s=q.get('savol',''); v=q.get('variantlar',[]); a=q.get('togri')
   if len(v)!=4 or type(a)!=int or not 0<=a<4: continue
   counts[a]+=1
   row={'file':p.relative_to(R).as_posix(),'n':i,'q':s,'v':v,'a':a}
   key=(g.name,p.parent.name,re.sub(r'\s+',' ',s).strip(),tuple(sorted(v)))
   groups[key].append(row)
   if re.search(r'rasm|jadval|chizma|quyidagi|hisoblang|nechaga teng',s,re.I):rows.append(row)
  m=p.parent/'_mavzular.json'
 dist[g.name]=dict(counts)
 samples[g.name]=rows[:8]
conflicts=[rs for rs in groups.values() if len(set(x['v'][x['a']] for x in rs))>1]
(O/'kalit_ziddiyatlari.json').write_text(json.dumps(conflicts,ensure_ascii=False,indent=2),encoding='utf-8')
print('CONFLICTS',len(conflicts))
print(json.dumps(conflicts[:18],ensure_ascii=False,indent=2))
print('DISTRIBUTION',dist)
print('SAMPLES',json.dumps(samples,ensure_ascii=False))
