from pathlib import Path
p=Path('audit/production_3sinf/fix_known_other_grades.py');s=p.read_text(encoding='utf-8');s=s[:s.index("edit(4,'Matematika'")];s=s.replace("folder.glob(prefix+'_*.json')","folder.glob(prefix+'.json')")
s+='''edit(4,'Matematika',"003_Ko'p xonali*",19,key=2)
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
 return '\\n'.join(out).rstrip()+'\\n'
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
 save(folder/'_TOLIQ.json',json.dumps(topics,ensure_ascii=False,indent=2)+'\\n')
(O/'changes.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
print('Other-grade confirmed corrections',len(ev))
'''
p.write_text(s,encoding='utf-8')
