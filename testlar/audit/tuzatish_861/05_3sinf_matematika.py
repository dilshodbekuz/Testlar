import csv,json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SRC=ROOT/'audit/qayta_3sinf/3_SINF_QOLGAN_MUAMMOLAR.csv'
BACKUP=ROOT/'audit/tuzatish_861/zaxira_3sinf_matematika'; JOURNAL=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'

# (fayl nomidagi boshlang'ich raqam, savol raqami): yangilanish
U={
('001',9):{'savol':"Sonlarni xonalar bo'yicha tagma-tag yozib qo'shish usuli qanday ataladi?"},
('014',2):{'savol':"Ko'paytirishni tekshirish uchun ko'paytma noldan farqli ko'paytuvchilardan biriga qanday amal qilinadi?"},
('015',1):{'savol':"Uch va undan ortiq ko'paytuvchini istalgan tartibda va guruhlab hisoblash qaysi xossalarga asoslanadi?",'variantlar':["Bo'lish xossasiga","Ko'paytirishning o'rin almashtirish va guruhlash xossalariga","Ayirish xossasiga","Qo'shishning o'rin almashtirish xossasiga"]},
('016',5):{'savol':"To'g'ri chiziqni bitta kichik lotin harfi bilan qanday belgilash mumkin?"},
('016',6):{'savol':"Ikki tomonga cheksiz davom etadigan tekis chiziq nima deyiladi?",'variantlar':["To'g'ri chiziq",'Aylana','Egri chiziq','Nuqta'],'togri':0},
('030',1):{'savol':"216:3 ni hisoblashda 2 yuzlik va 1 o'nlik jami nechta o'nlik bo'ladi?",'variantlar':["216 o'nlik","21 o'nlik","2 o'nlik","6 o'nlik"]},
('032',4):{'savol':"3 sonining barcha musbat karralilarini ketma-ket olish uchun 3 ni qaysi sonlarga ko'paytiramiz?"},
('032',21):{'savol':"72 sonini ikkita natural son ko'paytmasi ko'rinishida, tartibini hisobga olmay, necha usulda yozish mumkin?"},
('035',1):{'savol':"Uchala tomoni teng bo'lgan uchburchakning eng aniq nomi qaysi?"},
('042',5):{'savol':"Darslikda 10000 ichida sonlarni ustun shaklida qo'shish avval o'rganilgan qaysi bo'limdagi qo'shishga o'xshatib tushuntirilgan?"},
('042',20):{'savol':"Ulug'bek yulduz xaritasini tuzgan 1437-yilda necha yoshga to'lgan?"},
('043',3):{'savol':"Darslikda 10000 ichida sonlarni ustun shaklida ayirish avval o'rganilgan qaysi bo'limdagi ayirishga o'xshatib tushuntirilgan?"},
('043',25):{'savol':"Beruniy asari 1030-yilda yozilgan. Oradan 462 yil o'tib Kolumb Amerikaga yetib bordi. Bu qaysi yil?"},
('045',6):{'savol':"Rim raqamlarida I, X, C va M belgilari ketma-ket ko'pi bilan necha marta yoziladi?"},
('045',10):{'savol':"Ustki chiziqsiz odatiy rim yozuvida 3999 soni qanday yoziladi?"},
('045',29):{'savol':"Darslikda qo'llangan ustki chiziqsiz rim yozuvi qoidasiga ko'ra 4000 nega oddiy takrorlash bilan yozilmaydi?"},
('049',1):{'savol':"Ma'lum ko'paytuvchi noldan farqli bo'lsa, noma'lum ko'paytuvchini topish uchun nima qilinadi?"},
('052',8):{'savol':"Kattaliklarni qo'shish, ayirish yoki taqqoslashdan oldin ular qanday o'lchov birliklariga keltiriladi?"},
('056',8):{'savol':"Natural sonni 3 ga bo'lganda qoldiq qaysi son bo'la olmaydi?"},
('057',7):{'savol':"Qoldiqli bo'lishda bo'linuvchini qayta hosil qilib tekshirish uchun nima qilinadi?"},
('060',5):{'savol':"Aylana diametri yotgan to'g'ri chiziq aylana uchun nima bo'ladi?"},
('060',7):{'savol':"O'qda yotmaydigan ikki simmetrik nuqta simmetriya o'qiga nisbatan qanday joylashadi?"},
('060',10):{'savol':"Simmetrik uchburchaklarning mos uchlari nima yordamida tutashtiriladi?"},
('060',15):{'savol':"Uzunligi 5 cm bo'lgan kesmaning o'rta perpendikulari uni qanday ikki qismga ajratadi?"},
('061',28):{'savol':"Doira 12 teng bo'lakka bo'linib, 9 bo'lagi bo'yalgan. Bo'yalmagan qismni maxraji 12 bo'lgan kasr bilan yozganda surat nechaga teng?"},
('064',6):{'savol':"Aralash son qanday qismlardan iborat?",'variantlar':['Ikkita kasrdan','Faqat butun sondan','Faqat kasrdan',"Butun qism va to'g'ri kasr qismdan"]},
('070',1):{'savol':"Yuzalarni taqqoslashda o'lchovlar qanday birliklarda ifodalanishi kerak?",'variantlar':["Bir xil o'lchov birliklarida",'Faqat millimetrlarda',"Turli o'lchov birliklarida",'Faqat metrlarda']},
('073',6):{'savol':"Qaysi burchak o'tkir burchak deyiladi?",'variantlar':['90° dan katta','90° ga teng','180° ga teng','0° dan katta va 90° dan kichik']},
('073',7):{'savol':"Qaysi burchak o'tmas burchak deyiladi?",'variantlar':['90° dan katta va 180° dan kichik','180° ga teng','90° ga teng','0° dan katta va 90° dan kichik']},
('073',22):{'savol':"Boshlanish va tugash kunlarini ham sanab, 11-yanvardan 20-martgacha bo'lgan davr fevral 28 kun bo'lsa necha sutka?"},
('073',23):{'savol':"Boshlanish va tugash kunlarini ham sanab, 11-yanvardan 20-martgacha bo'lgan davr fevral 29 kun bo'lsa necha sutka?"},
('075',4):{'savol':"Maxraji 10, 100, 1000 kabi bo'lgan kasrni o'nli kasr shaklida yozishda nima qilinadi?",'variantlar':['Faqat maxraj yoziladi','Faqat vergul yoziladi',"Butun qism yozilib, verguldan keyin maxrajdagi nollar sonicha raqam yoziladi; zarur bo'lsa surat oldiga nol qo'yiladi",'Faqat surat yoziladi']},
('077',3):{'savol':"O'nli sanoq sistemasida har bir xona birligi o'zidan o'ngdagi keyingi xona birligidan qanday?"},
('078',8):{'savol':"Bo'linma va bo'luvchi yordamida bo'linuvchini qayta hosil qilish uchun qaysi amal bajariladi?"},
('079',1):{'savol':"Piramida asos tekisligidan tashqarida joylashib, barcha yon qirralar tutashadigan nuqta nima deyiladi?"},
('083',24):{'savol':"120 ta darslikning saqlanish holati tekshirildi: 1/20 qismi «3», 1/6 qismi «4», qolganlari «5» baho oldi. Nechta darslik «5» baho olgan?"},
}
rows=list(csv.DictReader(SRC.open(encoding='utf-8-sig'))); files={}; changes=[]
for r in rows:
 if r['fan']!='Matematika' or r['holat']!='tahrir':continue
 key=(Path(r['fayl']).name[:3],int(r['savol_raqami']))
 if key not in U:raise SystemExit(f'update yoq: {key}')
 p=ROOT/r['fayl'];data=files.setdefault(p,json.loads(p.read_text(encoding='utf-8')));q=data['savollar'][key[1]-1]
 before={**q,'variantlar':list(q['variantlar'])};q.update(U[key]);after={**q,'variantlar':list(q['variantlar'])}
 if before!=after:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_matematika_aniqlashtirish','fayl':r['fayl'],'savol_raqami':key[1],'oldin':before,'keyin':after,'manba':'3-sinf Matematika kitobi va audit izohi'})
for p,data in files.items():
 rel=p.relative_to(ROOT);b=BACKUP/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with JOURNAL.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes),'kutilgan',len(U))
