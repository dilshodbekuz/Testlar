#!/usr/bin/env python3
"""6-sinf rus tili 008 mavzusidagi buzilgan o'zbekcha izohlarni tiklaydi."""
import json, shutil
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'6-sinf/6-sinf 6-Sinf Rus tili/008_Как вежливо попросить.json'
B=ROOT/'audit/tuzatish_861/zaxira_6sinf_rus_tili'/P.relative_to(ROOT)
J=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'
B.parent.mkdir(parents=True,exist_ok=True)
if not B.exists(): shutil.copy2(P,B)
d=json.loads(P.read_text(encoding='utf-8-sig'))

# raqam: (savol, variantlar, to'g'ri indeks)
fix={
1:("«Анвар, купи эту книгу!» gapidagi fe'l qaysi shaxs va sonda?",["Birinchi shaxs birlik","Ikkinchi shaxs birlik","Uchinchi shaxs ko'plik","Birinchi shaxs ko'plik"],1),
2:("«Повелительное наклонение» o'zbek tilida qanday ataladi?",["Xabar mayli","Shart mayli","Buyruq mayli","Istak mayli"],2),
3:("«Ребята, купите учебники!» gapidagi fe'l qaysi sonda?",["Jamlovchi son","Birlik","Ko'plik","Tartib son"],2),
4:("«Пусть (пускай) Малика купит атлас» gapida ish-harakatni bajaruvchi qaysi shaxs?",["Birinchi shaxs","Uchinchi shaxs","Umumlashgan shaxs","Ikkinchi shaxs"],1),
5:("«Дружи с ней» gapidagi buyruq mayli fe'li qaysi sonda?",["Birinchi shaxs","Uchinchi shaxs","Ko'plik","Birlik"],3),
6:("«Читай» va «читайте» shakllari nimasi bilan farqlanadi?",["Zamoni bilan","Jinsi bilan","Soni va murojaat usuli bilan","Shaxsi bilan"],2),
7:("«Будьте добры!» birikmasi qanday ma'noni ifodalaydi?",["Savolni","Muloyim iltimosni","Hayratni","Qat'iy buyruqni"],1),
9:("«Если тебе не трудно...» birikmasi nima uchun ishlatiladi?",["Buyruq berish uchun","Xabar berish uchun","Undov uchun","Muloyim iltimos qilish uchun"],3),
10:("«Давай купим сборник рассказов» gapidagi «купим» fe'li qaysi shaxsda?",["Ikkinchi shaxs","Shaxssiz","Birinchi shaxs","Uchinchi shaxs"],2),
11:("«Я читаю книгу. И ты, Феруза, читай» namunasida ikkinchi gap nima ifodalaydi?",["Birgalikdagi taklifni","Zamon o'zgarishini","Buyruq yoki undovni","Fe'lning otga aylanishini"],2),
12:("«Бей — бейте» va «пей — пейте» juftliklarida ko'plik shakli qanday yasalgan?",["Old qo'shimcha bilan","-те qo'shimchasi bilan","Yumshoq belgi bilan","Fe'l negizi almashishi bilan"],1),
13:("«Встаю» fe'lidan «вставай, вставайте» buyruq shakllari qaysi vosita bilan yasalgan?",["-вай/-вайте qo'shimchalari bilan","So'z negizini tushirish bilan","Old qo'shimcha bilan","Zamon qo'shimchasi bilan"],0),
14:("«Закажите переписчику переписать текст» gapida nechta buyruq maylidagi fe'l bor?",["Bitta","Uchta","Ikkita","To'rtta"],0),
15:("«Не расставайся с ней» gapidagi «не» nima?",["Inkor yuklamasi","Bog'lovchi","Undov","Ko'makchi"],0),
16:("«Дай(те) мне книгу» shakllari nimasi bilan farqlanadi?",["Jinsi bilan","Birlik/ko'plik va murojaat usuli bilan","Ikkinchi/uchinchi shaxs bilan","Zamoni bilan"],1),
17:("«Посмотрю» fe'lidan «посмотрите» shakliga o'tganda fe'l qaysi maylga o'zgaradi?",["Xabar mayliga","Shart mayliga","Buyruq mayliga","Infinitivga"],2),
18:("«Дайте, пожалуйста, словарь» gapida «пожалуйста» qanday vazifa bajaradi?",["Iltimosni muloyimlashtiradi","Xabarni kuchaytiradi","Buyruqni qat'iylashtiradi","Savol hosil qiladi"],0),
19:("«Пусть твоё желание исполнится!» gapida istak qanday ifodalangan?",["Infinitiv bilan","Sifat bilan","«Пусть» va uchinchi shaxs fe'li bilan","Ot bilan"],2),
20:("«Что ты сделал бы, если бы стал волшебником?» gapida qaysi mayl ishlatilgan?",["Istak mayli","Xabar mayli","Shart mayli","Buyruq mayli"],2),
21:("Suhbatdoshning akasi kitobni olib kelishini qanday so'rash mumkin?",["Беги, бегите","Дай, дайте","Пусть его брат принесёт книгу","Давайте принесём"],2),
22:("Petrus Brovkaning «Не расставайся с ней. Дружи с ней» misralarida maslahat qaysi mayl orqali berilgan?",["Xabar mayli","Shart mayli","Infinitiv","Buyruq mayli"],3),
23:("«Пишу — пиши, пишите; смотрю — смотри, смотрите» namunasi nimani ko'rsatadi?",["Birinchi shaxs shaklidan buyruq mayli yasalishini","Fe'llarning otga aylanishini","Jins bo'yicha o'zgarishni","Faqat son bo'yicha o'zgarishni"],0),
24:("«Закажите переписчику переписать текст. Попросите художника нарисовать заглавные буквы» gaplarida nechta buyruq maylidagi fe'l bor?",["To'rtta","Bitta","Uchta","Ikkita"],3),
25:("«Брось — бросьте» va «отрежь — отрежьте» shakllarida qaysi imlo qoidasi ko'rinadi?",["Defis yozilishi","Tutuq belgisi yozilishi","Unli almashishi","Yumshoq belgi -те oldidan saqlanishi"],3),
26:("«Кто много читает, тот много знает. Немного читай, да много понимай!» gaplari qanday farqlanadi?",["Ikkalasi ham buyruq","Birinchisi xabar, ikkinchisi maslahat-buyruq","Ikkalasi ham savol","Ikkalasi ham shart"],1),
27:("«Дайте, пожалуйста, словарь» va «Вот книга, прочитай её» gaplarining asosiy farqi nima?",["Birinchisi savol, ikkinchisi xabar","Birinchisida inkor bor","Birinchisi o'tgan zamonda","Birinchi iltimos «пожалуйста» bilan muloyimlashtirilgan"],3),
28:("«Брошу — брось, бросьте; отрежу — отрежь, отрежьте» namunasi nimani ko'rsatadi?",["Sonlarning o'zgarishini","Zamonning o'zgarishini","Birinchi shaxs fe'lidan buyruq mayli shakllari yasalishini","Otning kelishikda o'zgarishini"],2),
29:("«Если тебе (вам) не трудно, ...» qolipi qanday nutqiy vazifani bajaradi?",["Iltimosni muloyim ifodalaydi","Zamonni bildiradi","Ko'chma ma'no hosil qiladi","Keskin buyruq beradi"],0),
30:("«Будьте добры! Будь добр!» va «Будьте любезны! Будь любезен!» birikmalarining umumiy jihati nima?",["Faqat ko'plikda ishlatiladi","Biri iltimos, biri buyruq","Barchasi muloyim iltimos qoliplaridir","Barchasi qat'iy buyruqdir"],2),
}
for n,(s,v,t) in fix.items():
 q=d['savollar'][n-1]; before=dict(q)
 q.update(savol=s,variantlar=v,togri=t)
 if q!=before:
  row={"vaqt":datetime.now().isoformat(timespec='seconds'),"fayl":str(P.relative_to(ROOT)),"savol_raqami":n,"oldin":before,"keyin":q,"sabab":"Buzilgan yoki noaniq o'zbekcha izoh rus tili darsligidagi misol va qoida asosida aniq yozildi","manba":"6-sinf Rus tili darsligi PDF"}
  with J.open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
P.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')

# Geografiyadagi javobi avval tuzatilgan savolning qolib ketgan buzilgan kesimi.
G=ROOT/"6-sinf/6-sinf 6-Sinf Geografiya/003_3- §. Geografik qobiqning chegaralari, xususiyatlari.json"
gd=json.loads(G.read_text(encoding='utf-8-sig')); gq=gd['savollar'][18]
gbefore=dict(gq)
gq['savol']="Yerdagi eng sodda organizmlar paydo bo'lgach, geografik qobiq rivojida qanday o'zgarish yuz berdi?"
if gq!=gbefore:
 GB=ROOT/'audit/tuzatish_861/zaxira_6sinf_rus_tili'/G.relative_to(ROOT)
 GB.parent.mkdir(parents=True,exist_ok=True)
 if not GB.exists(): shutil.copy2(G,GB)
 G.write_text(json.dumps(gd,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
 row={"vaqt":datetime.now().isoformat(timespec='seconds'),"fayl":str(G.relative_to(ROOT)),"savol_raqami":19,"oldin":gbefore,"keyin":gq,"sabab":"Buzilgan savol kesimi grammatik jihatdan tiklandi","manba":"6-sinf Geografiya darsligi PDF"}
 with J.open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print('tuzatildi',len(fix))
