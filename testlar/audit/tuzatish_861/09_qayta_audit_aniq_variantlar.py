import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl';B=ROOT/'audit/tuzatish_861/zaxira_qayta_audit'
U={
('5-sinf/5-sinf 5-Sinf Rus tili/010_9. Что видел ты в музее.json',11):{'savol':'В каком предложении глагол правильно употреблён в прошедшем времени?','variantlar':['Я иду в музей','Я пойду в музей','Я ходил в музей','Я хожу в музей'],'togri':2},
('6-sinf/6-sinf 6-Sinf Rus tili/013_Как ещё сказать о местонахождении предмета.json',9):{'savol':'«Санжар скрылся за ___». Вставьте нужную форму слова «забор».','variantlar':['заборе','забором','забора','забор'],'togri':1},
}
changes=[]
for (rel,n),patch in U.items():
 p=ROOT/rel;d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];before={**q,'variantlar':list(q['variantlar'])}
 b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 q.update(patch);after={**q,'variantlar':list(q['variantlar'])}
 changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'qayta_audit_takror_variant','fayl':rel,'savol_raqami':n,'oldin':before,'keyin':after,'manba':'Rus tili mavzusi va grammatika qoidasi'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
