import json,shutil,copy
from pathlib import Path
R=Path.cwd();O=R/'audit/production_known_fixes';O.mkdir(exist_ok=True);ev=[];folders=set()
def edit(g,subject,prefix,n,key=None,opt=None,encoding=False):
 folder=R/f'{g}-sinf'/f'{g}-sinf {g}-Sinf {subject}';p=next(folder.glob(prefix+'.json'));d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];bef=copy.deepcopy(q)
 if key is not None:q['togri']=key
 if opt is not None:q['variantlar'][opt[0]]=opt[1]
 if encoding:
  q['savol']=q['savol'].replace('shå','she').replace('Shå','She');q['variantlar']=[v.replace('shå','she').replace('Shå','She') for v in q['variantlar']]
 if q==bef:return
 b=O/'backup'/p.relative_to(R);b.parent.mkdir(exist_ok=True,parents=True)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');folders.add(folder)
 ev.append({'file':p.relative_to(R).as_posix(),'question_no':n,'before':bef,'after':q})
edit(4,'Matematika',"003_Ko'p xonali*",19,key=2)
edit(4,'Matematika','008_Uzunlik*',23,opt=(1,'25 m 64 cm'))
edit(6,'Matematika','003_Sonning*',11,opt=(2,'2 × 2 × 2'))
edit(6,'Matematika','003_Sonning*',14,opt=(0,'3 × 5 × 5'))
for n in [1,7,11,22]:edit(4,'Musiqa','001_Vatanimiz*',n,encoding=True)
def txt(d):
 out=[d['mavzu'],''];last=None
 for n,q in enumerate(d['savollar'],1):
  if q['qiyinlik']!=last:
   last=q['qiyinlik'];out+=['--- '+last.upper()+' ---','']
  out.append(str(n)+'. '+q['savol']);out.extend(('+' if j==q['togri'] else '')+'ABCD'[j]+') '+v for j,v in enumerate(q['variantlar']));out.append('')
 return '\n'.join(out).rstrip()+'\n'
def save(p,new):
 old=p.read_text(encoding='utf-8') if p.exists() else None
 if old==new:return
 b=O/'backup'/p.relative_to(R);b.parent.mkdir(exist_ok=True,parents=True)
 if p.exists() and not b.exists():shutil.copy2(p,b)
 p.write_text(new,encoding='utf-8')
for folder in folders:
 topics=[]
 for p in sorted(folder.glob('[0-9]*.json')):
  d=json.loads(p.read_text(encoding='utf-8'));topics.append(d);save(p.with_suffix('.txt'),txt(d))
 save(folder/'_TOLIQ.json',json.dumps(topics,ensure_ascii=False,indent=2)+'\n')
(O/'changes.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Other-grade confirmed corrections',len(ev))
