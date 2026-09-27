import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REL='3-sinf/3-sinf 3-Sinf O‘qish/020_Hunàrni såv.json';P=ROOT/REL
B=ROOT/'audit/tuzatish_861/zaxira_qayta_audit'/REL;J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
d=json.loads(P.read_text(encoding='utf-8'));B.parent.mkdir(parents=True,exist_ok=True)
if not B.exists():shutil.copy2(P,B)
changes=[]
for n,idx,new in [(1,0,'Qudrat Hikmat'),(7,1,'Zafar Diyor')]:
 q=d['savollar'][n-1];before={**q,'variantlar':list(q['variantlar'])};q['variantlar'][idx]=new;after={**q,'variantlar':list(q['variantlar'])}
 changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'takror_variant','fayl':REL,'savol_raqami':n,'oldin':before,'keyin':after,'manba':'savol muallifi variantlari'})
P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
