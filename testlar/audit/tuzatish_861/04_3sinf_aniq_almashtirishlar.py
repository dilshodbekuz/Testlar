import csv,json,re,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'audit/qayta_3sinf/3_SINF_QOLGAN_MUAMMOLAR.csv'
BACKUP=ROOT/'audit/tuzatish_861/zaxira_3sinf_aniq'
JOURNAL=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
pat=re.compile(r'«([^»]+)»\s*→\s*«([^»]+)»')
files={}; changes=[]
with SRC.open(encoding='utf-8-sig',newline='') as f:
 for row in csv.DictReader(f):
  if row['holat']!='tahrir':continue
  pairs=pat.findall(row['izoh'])
  if not pairs:continue
  p=ROOT/row['fayl']; n=int(row['savol_raqami'])
  data=files.setdefault(p,json.loads(p.read_text(encoding='utf-8'))); q=data['savollar'][n-1]
  before={**q,'variantlar':list(q['variantlar'])}
  def fix(s):
   for a,b in pairs:s=s.replace(a,b)
   return s
  q['savol']=fix(q['savol']);q['variantlar']=[fix(x) for x in q['variantlar']]
  after={**q,'variantlar':list(q['variantlar'])}
  if before!=after:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_aniq_almashtirish','fayl':row['fayl'],'savol_raqami':n,'oldin':before,'keyin':after,'manba':'3_SINF_QOLGAN_MUAMMOLAR.csv izohi'})
for p,data in files.items():
 rel=p.relative_to(ROOT); backup=BACKUP/rel;backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():shutil.copy2(p,backup)
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with JOURNAL.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan_savol',len(changes),'korilgan_fayl',len(files))
