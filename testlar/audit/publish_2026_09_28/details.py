import json
from pathlib import Path
R=Path.cwd()
for grade,subject,pattern,nums in [(4,'Musiqa','001_*',[1,7,11,22]),(6,'Matematika','003_*',[1,2,3,4,8,9,10,11,14]),(7,'Fizika','001_*',[10,20,30]),(8,'Algebra','001_*',[10,20,30]),(9,'Algebra','001_*',[10,20,30])]:
 for p in (R/f'{grade}-sinf'/f'{grade}-sinf {grade}-Sinf {subject}').glob(pattern+'.json'):
  d=json.loads(p.read_text(encoding='utf-8'));print(p.name, 'keys',list(d))
  for n in nums:
   if n<=len(d['savollar']):print(n,json.dumps(d['savollar'][n-1],ensure_ascii=False))
