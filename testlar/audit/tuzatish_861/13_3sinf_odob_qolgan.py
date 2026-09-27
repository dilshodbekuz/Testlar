import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl';B=ROOT/'audit/tuzatish_861/zaxira_3sinf_odob'
FILES={
'3-sinf/3-sinf 3-Sinf Odobnoma/002_Davlat ramzlari — milliy iftixorimiz.json':{
3:("O'zbekiston gerbida qaysi qush tasvirlangan?",['Burgut','Humo','Lochin','Laylak'],1),
5:("Xalqlar do'stligi maydonidagi bayroq ustunining balandligi necha metr?",['60','55','70','65'],3),
8:("G'alaba qozongan sportchilar davlat ramzlariga hurmatni qanday ifodalaydilar?",['Maydonni tark etadilar',"O'z davlatining bayrog'ini ko'taradilar",'Jim turadilar','Bayroqni yashiradilar'],1),
9:("Davlat madhiyasining asosiy vazifasi nima?",['Yurtga muhabbat va hurmatni ifodalash','Faqat matnni yodlash',"Yangi qo'shiq o'rganish",'Vaqt o‘tkazish'],0),
10:("Jaloliddin poytaxtga qaysi bayram arafasida keldi?",['Mustaqillik bayrami','Til bayrami',"Navro'z bayrami",'Xotira kuni'],0),
11:("O'ng qo'limizni ko'ksimizga qo'yish nimani bildiradi?",['Balandlikni',"Yurtga mehrimizni",'Shoshilayotganimizni','Kuchimizni'],1),
12:("Gerb va bayroqdagi har bir rang va tasvir nimani anglatadi?",['Tasodifiy bezakni',"O'ziga xos ramz va ma'noni",'Faqat tabiatni',"O'yinlarni"],1),
14:("Davlat ramzlariga hurmatsizlik qanday oqibatga olib keladi?",['Hech qanday oqibatga olib kelmaydi','Faqat ogohlantirishga','Darslik berilishiga',"Qonuniy javobgarlikka"],3),
17:("Madhiya yangraganda g'olib sportchilar nima qiladilar?",['Maydonda yuguradilar',"Davlat bayrog'ini baland ko'taradilar",'Maydonni tark etadilar','Raqsga tushadilar'],1),
18:("Jaloliddinning otasi bayroq haqida nima aytdi?",['Bayroq oddiy mato','Bayroq kerak emas','Bayroq yurt ozodligi va tinchligi ramzi','Bayroq faqat bezak'],2),
20:("Jaloliddin katta bo'lgach nima qilishini aytdi?",['Bayroq rasmini chizishni',"Yurt bayrog'ini yuksaklarga ko'tarishni",'Madhiya yozishni','Boshqa yurtga ketishni'],1),
21:("Nega davlat ramzlariga hurmatsizlik uchun qonunda javobgarlik ko'zda tutilgan?",['Ular eski bo‘lgani uchun','Hurmat shart emasligi uchun','Faqat rasmiy talab bo‘lgani uchun','Ular xalq birligi va davlat faxrini ifodalagani uchun'],3),
22:("Bayroq, gerb va madhiyaning jamiyat uchun birgalikdagi ahamiyati nimada?",['Faqat o‘quvchilarga kerak','Faqat ranglardan iborat','Milliy birlik va davlat mustaqilligini ifodalaydi','Faqat rasmiy bezak'],2),
23:("Jaloliddin nega bayroqni yuksaklarga ko'tarishni orzu qildi?",['Bayroq o‘yinchoq bo‘lgani uchun','Yurtga muhabbat va faxrini ifodalash uchun','Buni faqat qoida talab qilgani uchun','Boshqalarga taqlid qilish uchun'],1),
25:("Davlat madhiyasi yangraganda nega faxr va hayajon tuyg'ulari uyg'onadi?",['U faqat ohangdan iborat','U ranglarni tasvirlaydi','U oddiy qo‘shiq','U Vatan tarixi, qudrati va orzularini ifodalaydi'],3),
27:("O'ng qo'limizni ko'ksimizga qo'yish orqali nimani bildiramiz?",['Shoshayotganimizni','Qo‘limizni ko‘rsatishni','Faqat quvonchni','Yurtga chuqur muhabbat va hurmatni'],3),
28:("Davlat ramzlarini qachon hurmat qilish kerak?",['Har kuni va barcha tegishli vaziyatlarda','Faqat bayramlarda','Faqat maktabda','Hurmat qilish shart emas'],0),
29:("Nega bayroq azaldan g'alaba va ozodlik timsoli bo'lgan?",['U xalqning erkinligi va g‘alabasini ifodalagan','U faqat bezak bo‘lgan','U rang tanlash uchun ishlatilgan','U faqat sportda qo‘llangan'],0),
30:("Davlat gerbi, bayrog'i va madhiyasi o'zaro qanday bog'langan?",['Faqat tarixiyligi bilan','Ularning barchasi milliy birlik, mustaqillik va Vatanga muhabbatni ifodalaydi','Faqat rasmlari bilan','Faqat ranglari bilan'],1),
},
'3-sinf/3-sinf 3-Sinf Odobnoma/003_Tarixiy obidalar — madaniy boyligimiz.json':{
4:("Xiva shahrining 2500 yilligi qaysi yilda nishonlangan?",['1995-yilda','1996-yilda','1998-yilda','1997-yilda'],3),
5:("Oqsaroy ravog'ining oralig'i necha metrdan ortiq?",['15 metrdan','20 metrdan','22 metrdan','25 metrdan'],2),
9:("Registon maydonida nechta madrasa joylashgan?",['3 ta','4 ta','5 ta','2 ta'],0),
10:("Tarixiy obidalar bizga nima haqida darak beradi?",['Texnologiya haqida','Boy tariximiz va ajdodlarimiz aql-zakovati haqida',"Faqat qishloq xo'jaligi haqida",'Faqat savdo haqida'],1),
12:("Ichan qal'adagi qalin devorlar qanday vazifani bajargan?",['Xalqni tashqi dushmanlardan himoya qilgan','Ombor bo‘lgan',"Qal'ani bezagan",'Masofa o‘lchagan'],0),
14:("Oqsaroy peshtoqidagi yozuv nimani ifodalaydi?",['Temuriylarning osoyishtaligini','Faqat savdoni','Faqat boylikni','Temuriylar qudrati va bunyodkorlik mahoratini'],3),
17:("Xiva shahrining 2500 yilligi nishonlanganda qanday ish amalga oshirilgan?",['Yangi bozor ochilgan','Yangi madrasa qurilgan','Yangi minora qurilgan',"Ichan qal'a qayta ta'mirlangan"],3),
22:("Minorayi Kalon va Oqsaroyning asosiy farqi nimada?",['Ikkalasi bir xil inshoot','Ular orasida farq yo‘q','Ikkalasi ham madrasa','Minorayi Kalon minora, Oqsaroy esa saroy'],3),
23:("Registon maydoni nega muhim tarixiy obida hisoblanadi?",['U yerda ko‘p odam yashagani uchun','U yerda bozor bo‘lgani uchun','Uchta muhtasham madrasa xalqimiz madaniy merosidan darak bergani uchun','U yerda pul ko‘p bo‘lgani uchun'],2),
24:("Tarixiy obidalarni asrab-avaylash nima uchun zarur?",["Kelajak avlodga tariximizni bilish imkonini berish uchun",'Faqat odamlarni band qilish uchun','Faqat pul topish uchun','Faqat yangi bino qurish uchun'],0),
26:("Oqsaroy peshtoqidagi yozuv Temuriylarning qaysi fazilatini ko'rsatadi?",['Faqat boyligini','Faqat osoyishtaligini','Qudrati va bunyodkorlik mahoratini','Faqat savdogarligini'],2),
28:("Konstitutsiyadagi «Madaniyat yodgorliklari davlat muhofazasidadir» qoidasi nimani anglatadi?",['Obidalar faqat qadimgi odamlarning ishi','Har kim obidani buzishi mumkin','Obidalar o‘z-o‘zidan saqlanadi','Davlat yodgorliklarni saqlash va himoya qilish uchun mas’ul'],3),
29:("Mustaqillik yillarida qurilgan imoratlar kelajakda nima bo'lishi mumkin?",['Faqat rasm vositasi','Ahamiyatsiz inshoot','Faqat hozirgi davr binosi','Davrimiz madaniy taraqqiyotining dalili bo‘lgan tarixiy obida'],3),
30:("Matndagi «Buxoroga kelgan kishi Minorayi Kalonni ko'rmay ketmaydi» iborasi nimani ta'kidlaydi?",['Shaharning kattaligini','Minorayi Kalonning tarixiy va madaniy qadrini','Faqat sayyohlar sonini','Masofaning uzoqligini'],1),
},
'3-sinf/3-sinf 3-Sinf Odobnoma/005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json':{
1:("Ma'rifatparvarlik nima demak?",['Insonlarni yaxshi bo‘lishga chorlash','Insonlarni faqat ishlashga chorlash','Insonlarni boylik izlashga chorlash','Insonlarni bilim olishga chorlash'],3),
2:("Darslikda «Avesto»ning qaysi jihati ta'kidlangan?",['Urush va shijoat','Qushlar va hayvonlar',"Ilm o'rganish va odob-axloq",'Hunarmandchilik va savdo'],2),
3:("«Ezgu fikr, ezgu so'z, ezgu amal» qaysi kitobning bosh qoidasidir?",['Qadimgi Rim bitiklari','Hadis','Avesto',"Qur'on"],2),
4:("Ibn Sino qaysi fanlarni chuqur bilgan?",['Faqat tabiatshunoslik','Tabobat, matematika va tabiatshunoslik','Faqat tabobat','Faqat matematika'],1),
5:("Rivoyatga ko'ra, Beruniy yiliga necha marta dam olgan?",["Bir marta — Navro'zda",'Har hafta','Ikki marta — Navro‘zda va bug‘doyga birinchi o‘roq tushganda','Har oy'],2),
6:("Mirzo Ulug'bek qaysi ilm bilan shug'ullangan?",['Yulduzlar ilmi','Tarix','Tibbiyot',"O'qituvchilik"],0),
8:("«Najot» so'zi nimani anglatadi?",['Yaxshi bilim olishni',"Ko'mak, yordam, qiyin vaziyatdan chiqish yo'lini",'Tez harakatni','Uzoq safarni'],1),
9:("Arastu kim?",['Ilm-fanni rivojlantirgan qadimgi alloma','Yulduzlarni o‘rgangan shoh','Buyuk tabib','Davlat arbobi'],0),
10:("2017-yilda Hindistonda maktab o'quvchilari o'rtasida o'tkazilgan xalqaro matematika musobaqasining umumjamoa hisobida O'zbekiston nechanchi o'rinni egalladi?",["2-o'rin","5-o'rin","1-o'rin","3-o'rin"],0),
11:("Ibn Sino dastlab matematikani nega yoqtirmagan?",['Juda qiyin deb o‘ylagani uchun',"Vaqti bo'lmagani uchun",'Uni o‘rganmaganligi uchun',"O'qituvchisi bo'lmagani uchun"],0),
12:("Rivoyatga ko'ra, Beruniy Navro'z kuni nima qilgan?",["Tug'ilgan shahriga ketgan",'Yolg‘iz sayr qilgan',"Faqat kitob o'qigan",'Yuvinib-taranib, yaxshi libos kiyib, yor-u birodarlarini ziyorat qilgan'],3),
14:("Rivoyatga ko'ra, Beruniy yil davomida asosan nima bilan shug'ullangan?",["O'yin-kulgi",'Sayohat va savdo',"Mutolaa, kitob yozish, tajriba va ijod",'Har kuni bir xil ish'],2),
15:("Matnga ko'ra, qaysi mamlakat qudratli bo'ladi?",["Bilimli odamlari ko'p mamlakat","Askari ko'p mamlakat","Boylari ko'p mamlakat",'Hududi eng katta mamlakat'],0),
16:("Ibn Sino arqon va marmar tosh hikoyasidan qanday saboq oldi?",['Arqon yasashni','Tosh yo‘nishni',"Qiyin bo'lsa ham, g'ayrat va sabr bilan maqsadga erishishni",'Marmar qimmatligini'],2),
18:("Darslikda Mirzo Ulug'bek rasadxonasiga qanday baho berilgan?",["O'z davri uchun buyuk kashfiyot",'Tibbiyot maktabi','Oddiy bino','Moliyaviy markaz'],0),
20:("Texnika vositalari nima natijasida yaratiladi?",["Insoniyatning ming yillar davomida to'plagan bilim va tajribasi natijasida",'Faqat ayrim odamlar istagi bilan','Tayyor holda paydo bo‘ladi','Faqat jismoniy kuch bilan'],0),
21:("Nega ajdodlarimizning ma'rifatparvarlik ishlari bizga ibrat?",['Ular boy bo‘lgani uchun','Ular shamolni o‘rganganlari uchun','Ular faqat tibbiyotni bilganlari uchun','Ular bilim orqali insoniyatni rivojlantirib, abadiy qadriyatlar yaratganlari uchun'],3),
22:("Ibn Sino haqidagi hikoyadan qanday saboq olish mumkin?",["Sabr va g'ayrat bilan har qanday ilmni o'zlashtirish mumkin",'Quduq qazish eng muhim hunar','Matematika o‘qitilmasa ham bo‘ladi',"Tabib bo'lish oson"],0),
23:("Beruniyning dam olish odati uning vaqtga munosabati haqida nimani ko'rsatadi?",['U har kuni bir ishni takrorlagan','U doimo shoshilgan','U faqat uyda yotgan','U vaqtning har bir lahzasini qadrlagan'],3),
25:("Allomalarimiz ishlari bugungi O'zbekiston yoshlariga qanday ta'sir ko'rsatmoqda?",['Ularni faqat harbiylikka undaydi',"Fan olimpiadalarida g'olib bo'lish va nufuzli universitetlarda o'qishga ilhom beradi",'Ularni faqat savdoga undaydi','Ularni bekorchilikka o‘rgatadi'],1),
26:("«Vaqtni qadrlashni buyuk bobomizdan o'rganishimiz kerak» degan fikr nimani anglatadi?",['Vaqtning ahamiyati yo‘q','Vaqt qimmatli boylik, har bir lahzadan unumli foydalanish kerak','Vaqt oddiy narsa','Vaqt ko‘p bo‘lgani uchun qadrsiz'],1),
27:("Izzat-hurmat va shon-sharafga qanday erishiladi?",["Ilm o'rganib, uni ezgu ishlarda qo'llash orqali",'Faqat boylik to‘plash orqali','Faqat meros orqali','Shohlarni ziyorat qilish orqali'],0),
29:("Mamlakatimizda ilm-fanni rivojlantirishga katta e'tibor qaratilishidan maqsad nima?",['Odamlar fikrini o‘zgartirish','Faqat ayrim shaxslarni rivojlantirish',"Mamlakat qudratini oshirib, O'zbekiston yoshlarining dunyoda muvaffaqiyat qozonishiga yo'l ochish",'Yoshlarni ajratib qo‘yish'],2),
}}
changes=[]
for rel,updates in FILES.items():
 p=ROOT/rel;d=json.loads(p.read_text(encoding='utf-8'));b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 for n,(s,v,k) in updates.items():
  q=d['savollar'][n-1];bef={**q,'variantlar':list(q['variantlar'])};q.update(savol=s,variantlar=v,togri=k);aft={**q,'variantlar':list(q['variantlar'])}
  if bef!=aft:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_odob_qolgan','fayl':rel,'savol_raqami':n,'oldin':bef,'keyin':aft,'manba':'3-sinf Odobnoma va audit izohi'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
