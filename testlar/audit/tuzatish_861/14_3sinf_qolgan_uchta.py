import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl';B=ROOT/'audit/tuzatish_861/zaxira_3sinf_qolgan'
U={
('3-sinf/3-sinf 3-Sinf Odobnoma/001_O‘zbekiston Respublikasi — mustaqil davlat.json',25):{'savol':'Ro‘yxatga ko‘ra, qaysi shaxmatchi Javohir Sindorovdan kattaroq yoshda grossmeyster bo‘lgan?'},
('3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json',2):{'savol':'Feruza kim?','variantlar':['Direktor',"O'quvchi",'Sinf rahbari',"O'qituvchi"]},
("3-sinf/3-sinf 3-Sinf Tabiatshunoslik/001_Tabiatshunoslik nimani o'rganadi.json",6):{'variantlar':['Dengizlar',"Cho'llar",'Bulutlar','Daryolar']},
}
changes=[]
for (rel,n),patch in U.items():
 p=ROOT/rel;d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];bef={**q,'variantlar':list(q['variantlar'])};b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 q.update(patch);aft={**q,'variantlar':list(q['variantlar'])};changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_qolgan','fayl':rel,'savol_raqami':n,'oldin':bef,'keyin':aft,'manba':'audit izohi'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
