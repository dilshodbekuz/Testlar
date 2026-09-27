import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl';B=ROOT/'audit/tuzatish_861/zaxira_3sinf_manba'
U={
("3-sinf/3-sinf 3-Sinf Matematika/001_Ikki va uch xonali sonlarni xonadan o'tib qo'shish va ayiris.json",10):{'savol':"Darslikdagi masalada Toshkent–Samarqand yo'nalishida qatnovchi tezyurar poyezd qanday nomlangan?"},
("3-sinf/3-sinf 3-Sinf Matematika/013_Yig'indini songa bo'lish.json",5):{'savol':"86 : 2 ni xona qo'shiluvchilariga ajratib hisoblash uchun 86 qanday yoyiladi?"},
("3-sinf/3-sinf 3-Sinf Matematika/033_Ikki xonali songa ko'paytirish.json",1):{'savol':"12 · 15 ni hisoblashda 15 soni xona qo'shiluvchilari yig'indisi ko'rinishida qanday yoyiladi?"},
("3-sinf/3-sinf 3-Sinf Matematika/040_To'rt xonali sonlarni taqqoslash.json",10):{'savol':"Darslik ma'lumotiga ko'ra, Qadimgi Misrda hisobni osonlashtiruvchi qaysi moslama ishlatilgan?"},
("3-sinf/3-sinf 3-Sinf Matematika/042_10000 ichida sonlarni ustun shaklida qo'shish.json",6):{'savol':"Darslik ma'lumotiga ko'ra, Ulug'bek observatoriyasida nechta yulduz xaritasi tuzilgan?"},
("3-sinf/3-sinf 3-Sinf Matematika/043_10000 ichida sonlarni ustun shaklida ayirish.json",6):{'savol':"Darslik ma'lumotiga ko'ra, Beruniy Amerika qit'asi borligini bashorat qilgan asarini qaysi yilda yozgan?"},
("3-sinf/3-sinf 3-Sinf Matematika/046_Og'zaki ko'paytirish va bo'lish.json",10):{'savol':"Darslik ma'lumotiga ko'ra, 827-yilda al-Xorazmiy nimani hisoblab topgan?"},
("3-sinf/3-sinf 3-Sinf Matematika/051_Ko'paytirishni tekshirish.json",24):{'savol':"Masala shartiga ko'ra, laylak 2000 m balandlikda uchadi. Turna undan 2 marta, lochin 5 marta balandroq uchsa, turna va lochin balandliklari yig'indisi necha km?"},
("3-sinf/3-sinf 3-Sinf Matematika/056_Tenglamalar.json",5):{'savol':"Darslikdagi masala shartiga ko'ra, bitta odam bir sutkada necha kg havo yutadi?"},
("3-sinf/3-sinf 3-Sinf Matematika/057_Masalalar yechish.json",2):{'savol':"Darslikdagi jadvalga ko'ra, qaysi transport vositasi 1 soatda 120 km yo'l bosadi?"},
("3-sinf/3-sinf 3-Sinf Matematika/057_Masalalar yechish.json",3):{'savol':"Darslikdagi masala shartiga ko'ra, bitta odam bir sutkada necha kg havo yutadi?"},
("3-sinf/3-sinf 3-Sinf Matematika/057_Masalalar yechish.json",10):{'savol':"Masalada har biri 150 g bo'lgan 3 paket sabzi urug'i olingan. 3 · 150 g nimani bildiradi?"},
("3-sinf/3-sinf 3-Sinf Matematika/079_Fazoviy figura – piramida.json",7):{'savol':"Darslikdagi andazada o'rta chiziqlar bo'ylab buklab uchburchakli piramida hosil qilish uchun kartondan qaysi figura qirqiladi?"},
("3-sinf/3-sinf 3-Sinf Matematika/080_Konus va boshqa fazoviy figuralar.json",2):{'savol':"To'g'ri burchakli uchburchak bir kateti atrofida aylantirilib konus hosil qilinsa, konus asosining radiusi nimaga teng?"},
("3-sinf/3-sinf 3-Sinf Matematika/083_Yakuniy takrorlash.json",4):{'savol':"Ko'paytirish qoidasiga asoslangan sonli piramidada yuqoridagi son nimaga teng?"},
}
changes=[]
for (rel,n),patch in U.items():
 p=ROOT/rel;d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];bef={**q,'variantlar':list(q['variantlar'])};b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 q.update(patch);aft={**q,'variantlar':list(q['variantlar'])};changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_manba_aniqlashtirish','fayl':rel,'savol_raqami':n,'oldin':bef,'keyin':aft,'manba':'3-sinf Matematika PDF'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
