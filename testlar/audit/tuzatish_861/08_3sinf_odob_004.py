import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REL='3-sinf/3-sinf 3-Sinf Odobnoma/004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json';P=ROOT/REL
B=ROOT/'audit/tuzatish_861/zaxira_3sinf_odob'/REL;J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
d=json.loads(P.read_text(encoding='utf-8'));B.parent.mkdir(parents=True,exist_ok=True)
if not B.exists():shutil.copy2(P,B)
before_all=[{**q,'variantlar':list(q['variantlar'])} for q in d['savollar']]
repl={'kimsi':'kimi','qanday nomi bilan':'qanday nom bilan','Ayyoqa':'Boshqa','Eronga':'Erondan','Saroj':'Saroy','necha talabalar':'nechta talaba','Beshyuzga':'Besh yuzga','yoʻnib ishlay turgan':'yoʻnib bergan','Devalar':'Tuyalar','qayga':'qayerga','Shugunga':'Pastga','Yolga':"Yo'lga",'Kokga':"Ko'kka",'Xind':'Hind','Shahistar':'Boshqa savdo',"Aql-u zakovat tengsiz":"Aql-u zakovati tengsiz",'Armiya boshlamoq':"Qo'shinni boshqarish",'Taror ishlari':'Dehqonchilik ishlari','javobgarchi qildi':'javobgar qilib qo‘ydi','Keng maydonida':'Keng maydonda',"Tog'lilar":"Bog'lar",'Ziyonda olib keladi':'Zarar keltiradi',"Oʻzbekistoniga":"Oʻzbekistonga","O'rta turmush uchun":"Dam olish uchun",'mamlakatingiz barkatini':'mamlakat daromadini',"o'yg'otadi":"uyg'otadi",'Uchta-beshta talabalar tilgan edi':'Atigi bir necha talaba ta’lim olgan','Ishchilarni shartli qildi':'Ishchilarga aniq vazifa berdi','kokga':"ko'kka",'keng maydonida':'keng maydonda'}
for q in d['savollar']:
 for a,b in repl.items():
  q['savol']=q['savol'].replace(a,b);q['variantlar']=[x.replace(a,b) for x in q['variantlar']]
S={
4:"Hikoyaga ko'ra, Amir Temur 1399-yilda nima qurdirmoqchi bo'lgan?",
7:"Qurilishda og'ir yuklarni tashish uchun Hindistondan qaysi hayvonlar keltirilgan?",
8:"Hikoyaga ko'ra, Bibixonim madrasa yonida nima qurdirgan?",
12:"Bibixonim davlat ishlarida qanday rol o'ynagan?",
17:"Keng maydonda nima tiklangan?",
19:"Matnga ko'ra, chet ellik sayyohlar O'zbekistonga asosan nima uchun keladi?",
20:"Amir Temur shaharga qaytib, Bibixonim qurdirgan madrasa va masjidni ko'rganda qanday munosabat bildirgan?",
21:"Amir Temur nega madrasa qurilishiga rahbarlikni Bibixonimga topshirgan?",
23:"Bibixonimning masjidni bitirib, Amir Temurga sovg'a qilish niyati nimani ifodalaydi?",
24:"Chet ellik sayyohlarning tarixiy obidalarimizga qiziqishi mamlakat iqtisodiga qanday ta'sir qiladi?",
25:"Amir Temur va Bibixonim munosabatlarida qaysi fazilat namoyon bo'lgan?",
26:"Buyuk Ipak yo'li va tarixiy obidalar O'zbekistonga sayyohlarni qanday jalb qiladi?",
27:"Bibixonim madrasasining o'z davridagi asosiy ahamiyati nimada bo'lgan?",
28:"Qurilishda ho'kiz va fillardan foydalanish nima uchun samarali bo'lgan?",
29:"Quruvchilarga topshiriq va in'omlar berish qanday natija bergan?",
30:"Ko'kka cho'zilgan minoralar, oq marmar ravoqlar va masjid nimani ifodalaydi?",
}
V={
21:['Bibixonim eng yosh bo‘lgani uchun','Amir Temur qurilishdan charchagani uchun','Qurilish muhim bo‘lmagani uchun','Uning aql-zakovati va davlat ishlaridagi tajribasiga ishongani uchun'],
23:['Pulni behuda sarflashni','Shunchaki qurilish istagini','Amir Temurga sadoqati va hurmatini','Uni sinash niyatini'],
24:["Hech qanday ta'sir qilmaydi",'Sayyohlik daromadini oshirib, turizmni rivojlantiradi','Faqat mahalliy oyliklarni oshiradi',"Salbiy ta'sir qiladi"],
25:['O‘zaro hurmat va ishonchni','Faqat diniy munosabatni','Faqat xizmat munosabatini','Shunchaki qarindoshlikni'],
26:['Salbiy ta’sir qiladi','Yurtning qadimiy tarixini tanitib, sayyohlar qiziqishini oshiradi','Hech qanday bog‘liqlik yo‘q','Faqat qadimiy diyor degan nom beradi'],
27:['Faqat kambag‘al bolalar uchun bo‘lgan','Ahamiyatsiz qurilish bo‘lgan','Ko‘plab yoshlar ilm oladigan yirik ta’lim maskani bo‘lgan','Unda bir necha talaba o‘qigan'],
28:['Og‘ir toshlarni tashish va qurilishni tezlashtirishga yordam bergan','Hayvonlar ko‘p bo‘lgani uchun','Hindiston yaqin bo‘lgani uchun','Tog‘lar katta bo‘lgani uchun'],
29:['Faqat pul sarflangan','Ishchilar chalg‘igan','Qurilish to‘xtagan','Ish tezlashib, qurilish o‘z vaqtida bitgan'],
30:['Inshootlarning ulug‘vorligi va bunyodkorlik mahoratini','Pul ko‘pligini','Oddiy bir qurilishni','Vaqt behuda ketganini'],
}
for n,s in S.items():d['savollar'][n-1]['savol']=s
for n,v in V.items():d['savollar'][n-1]['variantlar']=v
# 25-savol yangi variantlarida to'g'ri javob A ga ko'chdi.
d['savollar'][24]['togri']=0
changes=[]
for n,(bef,q) in enumerate(zip(before_all,d['savollar']),1):
 aft={**q,'variantlar':list(q['variantlar'])}
 if bef!=aft:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_odob_004','fayl':REL,'savol_raqami':n,'oldin':bef,'keyin':aft,'manba':'3-sinf Odobnoma va audit izohi'})
P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
