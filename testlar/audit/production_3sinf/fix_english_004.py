import json,copy,shutil,hashlib
from pathlib import Path
R=Path.cwd();O=R/'audit/production_3sinf';p=next((R/'3-sinf/3-sinf 3-Sinf Ingliz tili').glob('004_*.json'));d=json.loads(p.read_text(encoding='utf-8'));ev=json.loads((O/'changes_applied.json').read_text(encoding='utf-8'))
U={
1:("'Our family is big' mavzusida nima haqida gap bor?",["Uy haqida","Oila haqida","Do'stlar haqida","Maktab haqida"],1),
2:("'Make my family photo album' topshirig'ida nima qilish so'ralgan?",["Oila fotoalbomini yaratish","Maktab rasmini chizish","So'zlarni alifbo tartibida yozish","Kitob o'qish"],0),
3:("Loyiha ko'rsatmasi: '1a. Make my family photo album.' Bu bosqichda nima qilinadi?",["Faqat gaplar tarjima qilinadi","Tayyor albom taqdim etiladi","O'yin o'ynaladi","Oila fotoalbomi yaratiladi"],3),
4:("'This is my sister. Her name is Odina.' Gaplarga ko'ra, Odina so'zlovchiga kim bo'ladi?",["Onasi","Opasi yoki singlisi","Xolasi","Akasi yoki ukasi"],1),
5:("'Her name is Odina. She is 25.' Gaplarga ko'ra, Odina necha yoshda?",None,2),
6:("'Odina is a secretary' gapiga ko'ra, Odina kim bo'lib ishlaydi?",["Shifokor","O'qituvchi","Kotiba","Sotuvchi"],2),
7:("'Madina has two brothers' gapiga ko'ra, Madinaning nechta aka yoki ukasi bor?",["Ikkita","Uchta","To'rtta","Bitta"],0),
8:("'Present your family photo album' topshirig'i nimani bildiradi?",["Oila fotoalbomingizni taqdim eting","Fotoalbomni yoping","O'yin o'ynang","Matnni ko'chiring"],0),
9:("Fotoalbomdagi 'Contents' so'zi nimani bildiradi?",None,0),
10:("Loyiha topshirig'i: 'Play Madina has two brothers'. Nima qilish so'ralgan?",["Shu nomli o'yinni o'ynash","Rasm chizish","Albomni yopish","Kitob sotib olish"],0),
11:("Albom mundarijasida besh xil oila a'zosi uchun bittadan band bor: 'My dad', 'My mum' va yana uchta band. Jami nechta oila a'zosi ko'rsatilgan?",None,0),
12:("Matn: 'This is my sister. Her name is Odina. She is a secretary. She is 25.' Nechta ma'lumot aytilgan: qarindoshligi, ismi, kasbi va yoshi?",None,3),
13:("Mundarija: 1. My dad; 2. My mum; 3. My sister. Birinchi band qaysi?",None,1),
14:("Mundarija: 1. My dad; 2. My mum; 3. My sister. Ikkinchi band qaysi?",None,3),
15:("Matn: 'This is my sister. Her name is Odina. She is a secretary. She is 25.' Birinchi gap qaysi?",None,2),
16:("'This is my sister' gapi Odinaning qaysi jihatini bildiradi?",["So'zlovchiga qarindoshligini","Yoshini","Manzilini","Kasbini"],0),
17:("'Madina has two brothers' gapida nima aytilgan?",["Madinaning aka-ukalari soni","Madinaning yoshi","Madinaning manzili","Madinaning kasbi"],0),
18:("Madinaning ikkita aka-ukasi bor. Madina va uning ikki aka-ukasi birgalikda necha kishi bo'ladi?",None,2),
19:("Opa yoki singilni tanishtirish uchun qaysi gap mos?",["My dad is a teacher.","This is my sister.","This is my brother.","This is my mum."],1),
20:("Jasur Sobirov albomiga 'My family' deb nom qo'ydi. Albom nima haqida?",["Maktab haqida","Darslar haqida","Oila haqida","Do'stlar haqida"],2),
21:("Oila fotoalbomida 'My dad' va 'My mum' bandlari bor. Qaysi qatordagi uchta band ham qarindoshlar haqida?",None,3),
22:("'Our family is big' mavzusida oila fotoalbomini tayyorlash nimani mashq qilishga yordam beradi?",["Oila a'zolarini ingliz tilida tanishtirishni","Faqat sinf jihozlarini sanashni","Faqat albom o'lchamini hisoblashni","Transport nomlarini o'rganishni"],0),
23:("Loyiha bosqichlari: 1a — albom yaratish, 1b — tayyor albomni taqdim etish. Ish qanday tartibda bajariladi?",None,1),
24:("Albomda beshta oila a'zosining har biriga bittadan sahifa ajratildi. Muqova va mundarijani hisoblamaganda, ular uchun jami nechta sahifa kerak?",["4 sahifa","5 sahifa","3 sahifa","6 sahifa"],1),
25:("'This is my sister. Her name is Odina. She is a secretary. She is 25.' Bu matnning shakli qanday?",["Hisoblash misoli","Uzun maqola","Faqat so'zlar ro'yxati","Qisqa tanishtiruv"],3),
26:("'Madina has two brothers' qolipi bo'yicha Alining bitta opa-singli borligini qanday aytamiz?",["Ali have one sister.","Ali has two brothers.","Ali is one sister.","Ali has one sister."],3),
27:("Loyihada avval oila fotoalbomi yaratiladi, keyin shu albom taqdim etiladi. Bosqichlar qanday bog'langan?",["Birinchi bosqichda tayyorlangan albom ikkinchi bosqichda taqdim etiladi","Albom faqat taqdimotdan keyin yaratiladi","Bosqichlar bir-biriga aloqasiz","Ikkala bosqichda ham faqat kitob o'qiladi"],0),
28:("Albomdagi to'rtta bandning har biri 'My' so'zi bilan boshlanadi. Shu bandlar sarlavhalarida 'My' jami necha marta yoziladi?",None,2),
29:("Oila a'zosini tanishtirishda uning qarindoshligi, ismi, kasbi va yoshini aytish qolipidan boshqa oila a'zolari uchun ham foydalanish mumkinmi?",None,0),
}
b=O/'backup'/p.relative_to(R);b.parent.mkdir(exist_ok=True,parents=True)
if not b.exists():shutil.copy2(p,b)
for n,(s,v,a) in U.items():
 q=d['savollar'][n-1];before=copy.deepcopy(q);q['savol']=s;q['togri']=a
 if v:q['variantlar']=v
 assert len(set(q['variantlar']))==4
 if before!=q:ev.append({'file':p.relative_to(R).as_posix(),'question_no':n,'before':before,'after':copy.deepcopy(q),'reason':'Mahalliy Ingliz tili PDF 7-bet: noto‘g‘ri tarjima, yetishmayotgan shart va noaniq javoblar tuzatildi'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(O/'changes_applied.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger=json.loads((O/'review_ledger.json').read_text(encoding='utf-8'));idx={(x['file'],x['question_no']):x for x in ledger}
for n,q in enumerate(d['savollar'],1):
 x=idx[(p.relative_to(R).as_posix(),n)];x.update(status='joriy_tekshirildi',sha256=hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),evidence='Mahalliy Ingliz tili PDF 7-bet ko‘z bilan ko‘rildi; barcha variantlar va kalit tekshirildi. 29 savol saqlandi; sun’iy to‘ldirilmadi.')
(O/'review_ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Reviewed 29; corrected',len(U),'total unique corrections',len({(x['file'],x['question_no']) for x in ev}))
