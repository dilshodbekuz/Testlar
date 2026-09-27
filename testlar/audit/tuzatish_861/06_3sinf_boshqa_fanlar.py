import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];BACKUP=ROOT/'audit/tuzatish_861/zaxira_3sinf_boshqa';JOURNAL=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
U={
('3-sinf/3-sinf 3-Sinf Ingliz tili/001_Unit 1 Lesson 1 I have two sisters.json',3):{'variantlar':['Togalar','Onalar','Akalar yoki ukalar','Opalar yoki singillar']},
('3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json',2):{'variantlar':['Direktor',"O'quvchi",'Sinf rahbari',"O'qituvchi"]},
('3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json',9):{'savol':'Maktab direktori kim?'},
("3-sinf/3-sinf 3-Sinf O‘qish/005_Mahallam ajib ko'rkam.json",8):{'savol':"Mahallada bolalar qanday o'yinlar bilan shug'ullanadi?",'variantlar':["Kompyuter o'ynashadi","Kitob o'qishadi","Ko'zboylag'ich, bekinmachoq va soqqa",'Dars yozadi']},
("3-sinf/3-sinf 3-Sinf Tabiatshunoslik/001_Tabiatshunoslik nimani o'rganadi.json",6):{'variantlar':['Dengizlar',"Cho'llar",'Bulutlar','Daryolar']},
("3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json",5):{'savol':"O'ng qo'l qoidasi qanday vaziyatda qo'llanadi?",'variantlar':["Faqat yo'lda",'Faqat oshxonada',"Faqat o'yinda","Biror ishni boshlash yoki navbatni aniqlashda"]},
("3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json",6):{'savol':"Tanaffusda o'quvchi o'zini qanday tutishi kerak?",'variantlar':['Yugurib boshqalarga xalaqit berishi',"Baland ovozda baqirishi",'Kechikib kelishi',"Boshqalarning dam olishiga xalaqit bermasligi"]},
("3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json",7):{'savol':"Rasm ishlashda to'g'ri o'tirish holati qaysi?",'variantlar':["Gavdani tik tutib, stolga me'yorida yaqin o'tirish","Orqaga yastanib o'tirish","Gavdani burib o'tirish","Yotib ishlash"]},
("3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json",10):{'variantlar':["Rasm, haykal, relyef va boshqa san'at asarlarini yaratadi","Faqat sport o'rgatadi",'Faqat haykal yasaydi','Faqat rasm ishlaydi']},
("3-sinf/3-sinf 3-Sinf Texnologiya/001_«Kuz» manzarasini applikatsiya usulida yasash.json",8):{'savol':'Applikatsiya yasash qaysi bosqichdan boshlanadi?'},
("3-sinf/3-sinf 3-Sinf Texnologiya/001_«Kuz» manzarasini applikatsiya usulida yasash.json",9):{'variantlar':["Qog'ozdan qirqib",'Chizib','Loydan yasab','Shaklga solib']},
}
changes=[]
for (rel,n),patch in U.items():
 p=ROOT/rel;data=json.loads(p.read_text(encoding='utf-8'));q=data['savollar'][n-1];before={**q,'variantlar':list(q['variantlar'])}
 b=BACKUP/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 q.update(patch);after={**q,'variantlar':list(q['variantlar'])}
 if before!=after:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_boshqa_fan','fayl':rel,'savol_raqami':n,'oldin':before,'keyin':after,'manba':'3-sinf kitobi va audit izohi'})
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with JOURNAL.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
