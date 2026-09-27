import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REL='3-sinf/3-sinf 3-Sinf Odobnoma/006_Odob-axloq me’yorlari.json';P=ROOT/REL
B=ROOT/'audit/tuzatish_861/zaxira_3sinf_odob'/REL;J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
# savol, variantlar, to'g'ri indeks
U={
1:("Luqmon odobni kimdan o'rgangan?",['Bobosidan','Oqil kishidan','Ota-onasidan','Odobsiz kishilardan'],3),
2:("Sohibqiron Amir Temur xalqni o'ziga rom qilish uchun qaysi fazilatlardan foydalanganini aytgan?",['Kuch va jahldan','Jabr-zulmdan','Ochiq yuzlilik va rahm-shafqatdan','Qo‘pollikdan'],2),
3:("Halol bo'lish nimani anglatadi?",['Hiyla ishlatishni','Rostgo‘y bo‘lib, mehnat bilan yashashni','Boshqalarga zarar berishni',"Yolg'on gapirishni"],1),
4:("Donishmand farzandiga yalqovlikdan uzoqlashish haqida nima degan?",['Yalqovlik yaxshi odat',"Ishlamasa ham bo'ladi", "G'ayrat-shijoatni o'zingga shior qil", "Uyda o'tirish kerak"],2),
5:("Donishmand ehtiyotkorlikka oid qanday nasihat bergan?",['Doimo shubhalan','Barcha ishda tartib va intizomga rioya qil','Boshqalarning ishiga aralash','Boshqalardan shikoyat qil'],1),
6:("Samimiy va pok qalbli bo'lish nimani anglatadi?",["Yolg'on gapirishni",'Har safar fikrni o‘zgartirishni',"To'g'ri va halol o'ylab, gapirishni",'Boshqalarga yordam bermaslikni'],2),
7:("Nega ilmli kishilar bilan do'st bo'lish yaxshi?",['Ular boy bo‘lgani uchun',"Ular ilm-u odob bilan hayot kechirgani uchun",'Ular qiyinchilik tug‘dirgani uchun',"Ularning puli ko'p bo‘lgani uchun"],1),
8:("Olijanob kishi do'stining aybini yolg'iz qolganda nima qiladi?",["Do'stiga aytib, tuzatishga yordam beradi",'Dushmanlariga aytadi','Hammaga oshkor qiladi','Har kimga gapirib yuradi'],0),
9:("Mard va jasur kishi do'stlikdan nimani kutmaydi?",['Manfaat va foyda','Samimiyat','Sadoqat','O‘zaro yordam'],0),
10:("Kaykovus yangi do'st topganda eski do'stga qanday munosabatda bo'lishni aytgan?",['Uni mensimaslikni','Uni yomonlashni',"Uni unutib, yuz o'girishni",'Uni ham qadrlashni'],3),
11:("Birovning nojo'ya xatti-harakati e'tiroz uyg'otsa, bundan qanday ibrat olish kerak?",['Indamaslik kerak','Uni yomonlash kerak',"Bunday ishni o'zim qilmasligim kerak",'Buning ahamiyati yo‘q'],2),
12:("Donishmand halol mehnat haqida nimani tavsiya qilgan?",['Halol mehnat faqat ayrim kishilar uchun',"Halol mehnat qilgan odam kam bo'lmaydi",'Halol mehnat kerak emas','Halol mehnat faqat boylarga kerak'],1),
13:("«G'ayrat-shijoatni o'zingga shior qil» degan nasihat nimani talab qiladi?",["Doimo harakatda bo'lish va oldinga intilishni", "Doimo uyda o'tirishni",'Boshqalardan shikoyat qilishni','Erkalik qilishni'],0),
14:("Donishmand nima uchun «Senga topshirilgan vazifalarni bekam-ko'st ado qil» degan?",['Ishni to‘liq va puxta bajarish uchun','Ishni boshqalarga ko‘rsatish uchun','Ishni oshkor qilish uchun','Vaqt o‘tkazish uchun'],0),
15:("Donishmandning barcha nasihatlari asosan qaysi maqsadga qaratilgan?",['Odobli bo‘lib, hayotda yutuqqa erishishga',"Faqat o'rganishga",'Boshqalarni buzishga','Faqat pul topishga'],0),
16:("Alisher Navoiy nodon do'st haqida nima degan?",['Uning zarari ko‘proq bo‘lishi mumkin','U doimo rivojlantiradi','U samimiy bo‘ladi','U faqat foyda keltiradi'],0),
17:("Ilmli kishilardan qanday ibrat olish mumkin?",['Faqat pul topishni',"Faqat kitob o'qishni",'Ilm-u odob bilan yashashni',"Faqat jasur bo'lishni"],2),
18:("Matnda yangi do'st topganda eski do'stlar haqida nima deyilgan?",["Eski do'stlarni unutish",'Ulardan shikoyat qilish',"Faqat yangi do'st bilan yurish",'Eski do‘stlarni qadrlab, do‘stlar safini kengaytirish'],3),
19:("Amir Temur chin do'st ranjitsa ham nima qilish kerakligini aytgan?",['Uzrini qabul qilish','Undan o‘ch olish',"Yuz o'girish",'Doimo ranjib yurish'],0),
20:("Donishmandning barcha nasihatlaridagi umumiy jihat nima?",['Halol mehnat va odob-axloq','Pul topish',"Kuchga ega bo'lish",'Dunyoni o‘zgartirish'],0),
21:("«Odobni odobsizdan o'rgan» degan naql qanday o'rganish usulini ko'rsatadi?",["Faqat kitobdan o'rganishni",'Boshqalarni masxara qilishni',"Faqat yaxshi misoldan o'rganishni",'Salbiy misoldan xulosa chiqarishni'],3),
22:("Amir Temurning «Adolat bilan ish yuritib, jabr-zulmdan uzoq bo'lish» nasihati qaysi qadriyatga bog'liq?",['Adolatga','Zulmga','Manfaatga','Kuchga'],0),
23:("«Halol mehnat qil» va «Yalqovlikdan uzoqlash» nasihatlari birgalikda nimaga undaydi?",['Bekorchilikka',"Uyda o'tirishga",'Faol bo‘lib, mehnatni sevishga',"Faqat o'qishga"],2),
24:("Barcha ishda tartib-intizom va ehtiyotkorlikka rioya qilish qaysi maqsadga xizmat qiladi?",['Vaqt o‘tkazishga','Boshqalarni bezashga','Bekor yurishga',"Ishlarni to'g'ri va samarali bajarishga"],3),
25:("Samimiyat, pok qalb va to'g'riso'zlik o'rtasida qanday bog'lanish bor?",['Ular qarama-qarshi xususiyatlar','Ulardan bittasi yetarli',"Hammasi yaxshi do'st fazilatlaridir",'Ular faqat bahorda kerak'],2),
26:("Nega olijanob kishi do'stining aybini yolg'iz qolganda aytadi?",['Sir saqlash uchungina',"Do'stini xijolat qilmay, tuzalishiga yordam berish uchun",'Aybni yashirish uchun','Uni kamsitish uchun'],1),
27:("Matnda kimlar bilan do'st bo'lish tavsiya etilgan?",['Ilmli, olijanob va mard kishilar bilan','Hech kim bilan','Faqat olijanob kishi bilan','Faqat ilmli kishi bilan'],0),
28:("«Yaxshi do'stlar kishining boyligidir» degan so'zning ma'nosi nima?",["Do'stlar pul beradi",'Do‘st pulning yarmi',"Yaxshi do'stlar insonning ma'naviy tayanchidir",'Boylik faqat puldan iborat'],2),
29:("Halol mehnat qiladigan va odobli kishi do'stlariga qanday munosabatda bo'lishi kerak?",['Ularni mensimasligi','Ulardan yuz o‘girishi','Faqat foyda kutishi',"Yangi do'st orttirib, eski do'stlarini ham qadrlashi"],3),
30:("Donishmand nasihatlari va do'st tanlash qoidalarining asosiy fikri nima?",["Faqat kuchli bo'lish",'Boylikni hamma narsadan ustun qo‘yish',"Bitta do'st bilan cheklanish",'Odob-axloq, samimiyat va mehnat asosida yashash'],3),
}
d=json.loads(P.read_text(encoding='utf-8'));B.parent.mkdir(parents=True,exist_ok=True)
if not B.exists():shutil.copy2(P,B)
changes=[]
for n,(s,v,k) in U.items():
 q=d['savollar'][n-1];before={**q,'variantlar':list(q['variantlar'])};q.update(savol=s,variantlar=v,togri=k);after={**q,'variantlar':list(q['variantlar'])}
 if before!=after:changes.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'3sinf_odob_006','fayl':REL,'savol_raqami':n,'oldin':before,'keyin':after,'manba':'3-sinf Odobnoma va audit izohi'})
P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with J.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan',len(changes))
