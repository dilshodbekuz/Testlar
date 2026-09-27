import json,re,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SRC=ROOT/'audit/qayta_foydalanuvchi_tuzatganidan_keyin/avtomatik_topilmalar.jsonl'
B=ROOT/'audit/tuzatish_861/zaxira_eski_shrift';J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
# 3-sinf darslik PDFida eski shrift gliflari matn qatlamida quyidagicha chiqqan.
MAP=str.maketrans({'à':'a','î':'o','å':'e','ì':'i','ò':'o','õ':'x','â':'a','è':'e','û':'u','ô':'o','ù':'u',
                   'À':'A','Î':'O','Å':'E','Ì':'I','Ò':'T','Õ':'X','Â':'A','È':'E','Û':'U','Ô':'O','Ù':'U','�':''})
rows=[json.loads(x) for x in SRC.read_text().splitlines()]
targets=[]
for r in rows:
 if r['code']!='text_encoding':continue
 grade=r['file'].split('/')[0]
 # 8-sinfdagi Adèle va 7-sinfdagi Å qonuniy yozuvlar; ularga tegilmaydi.
 if grade in {'7-sinf','8-sinf'}:continue
 targets.append(r)
files={};changes=[]
for r in targets:
 p=ROOT/r['file'];data=files.setdefault(p,json.loads(p.read_text(encoding='utf-8')));n=r['question_no'];q=data['savollar'][n-1]
 before={**q,'variantlar':list(q['variantlar'])}
 q['savol']=q['savol'].translate(MAP);q['variantlar']=[x.translate(MAP) for x in q['variantlar']]
 after={**q,'variantlar':list(q['variantlar'])}
 if before!=after:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'eski_shrift_kodini_lotinlashtirish','fayl':r['file'],'savol_raqami':n,'oldin':before,'keyin':after,'manba':'3-sinf darslik PDF matn qatlamidagi glif mosligi'})
for p,data in files.items():
 rel=p.relative_to(ROOT);b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes),'fayl',len(files))
