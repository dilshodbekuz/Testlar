import json, shutil
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BACKUP=ROOT/'audit/tuzatish_861/zaxira_mazmun'
JOURNAL=ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl'

updates={
"4-sinf/4-sinf 4-Sinf Matematika/007_Qo'shishning o'rin almashtirish va guruhlash xossasi.json":{
5:{"savol":"500 + 800 + 500 yig'indisini qulay hisoblash uchun qaysi ikki qo'shiluvchini avval qo'shish ma'qul?","variantlar":["500 va 800 ni","800 va 500 ni","Ikkita 500 ni","Faqat 800 ni"],"togri":2}},
"5-sinf/5-sinf 5-Sinf Ingliz tili/010_UNIT 10 Wildlife.json":{
19:{"savol":"To'qay o'rmonlarida quyidagi hayvonlardan qaysi birini uchratish mumkin?","variantlar":["Pingvinlarni","Oq ayiqlarni","Kengurularni","Tipratikanlarni"],"togri":3}},
"5-sinf/5-sinf 5-Sinf Musiqa/019_6-dars. Musiqali drama.json":{
29:{"savol":"Yunus Rajabiy, Sayfi Jalil va boshqalar musiqali drama janrining qaysi davr kompozitorlari?","variantlar":["Matndan aniqlab bo'lmaydi","To'xtasin Jalilovdan oldingi","To'xtasin Jalilovdan keyingi","Tolibjon Sodiqov va R. Glier bilan ayni bir davrdagi"],"togri":2}},
"5-sinf/5-sinf 5-Sinf Tarixdan hikoyalar/005_Qoyatosh suratlari.json":{
9:{"savol":"O'zbekistonda qoyatosh suratlari qaysi ikki asosiy usulda ishlangan?","variantlar":["Qog'ozga siyoh bilan chizish va bosish orqali","Toshni eritish va quyish orqali","Loydan shakl yasash va pishirish orqali","Urib-cho'kichlash va tabiiy bo'yoqlar bilan ishlash orqali"],"togri":3}},
"6-sinf/6-sinf 6-Sinf Adabiyot (2-qism)/010_Tog'ay Murod.json":{
24:{"variantlar":["Sho'ro adabiyotini yozib, hammani tanqid qilish","Oddiy xalqning unutilib borayotgan ruhiy boyliklarini asrab qolish","Qadimiy urf-odatlarni modernizm bilan birlashtirib yozish","Siyosiy masalalar haqida asarlar yozish"],"togri":1}},
"6-sinf/6-sinf 6-Sinf Fizika/014_Paskal qonuni va uning qo'llanilishi.json":{
4:{"variantlar":["Quvur va klapan","Porshenli ikkita silindr","Klapan va richaglar","Nasos va turbina"],"togri":1},
10:{"variantlar":["Nasos va motorni","Ikkita porshenni","Ikkita silindrni","Klapan va rostlagichni"],"togri":2}},
"6-sinf/6-sinf 6-Sinf Geografiya/024_26- §. Materik aholisi va uning tabiatga ta'siri.json":{
23:{"savol":"Afrikaning turli sohillarida aholi zich, materikning katta ichki qismlarida esa siyrak joylashgan. Buning asosiy sababi nima?"}},
"7-sinf/7-sinf 7-Sinf Adabiyot/005_Mardlik afsonasi.json":{
27:{"variantlar":["Donolik, mehr va so'zining qadri","Faqat jismoniy kuchi","Faqat boyligi","Faqat nasl-nasabi"],"togri":0}},
"6-sinf/6-sinf 6-Sinf Geografiya/005_5- §. Litosfera.json":{
10:{"savol":"Abissal mintaqa okean tubining qaysi chuqurlik oralig'ida joylashgan?","togri":0},
15:{"savol":"Batial mintaqa okean tubining qaysi chuqurlik oralig'ida joylashgan?","variantlar":["6000 m dan chuqur","200-3000 m","0-200 m","3000-6000 m"],"togri":1}},
}

changes=[]
for rel,qs in updates.items():
 p=ROOT/rel; data=json.loads(p.read_text(encoding='utf-8'))
 backup=BACKUP/rel; backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():shutil.copy2(p,backup)
 for n,patch in qs.items():
  q=data['savollar'][n-1]; before=dict(q); before['variantlar']=list(q['variantlar'])
  q.update(patch); after=dict(q); after['variantlar']=list(q['variantlar'])
  if before!=after:changes.append({"vaqt":datetime.now().isoformat(timespec='seconds'),"tur":"mazmun_yoki_kalit","fayl":rel,"savol_raqami":n,"oldin":before,"keyin":after,"manba":"Kitoblar PDF"})
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with JOURNAL.open('a',encoding='utf-8') as f:
 for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('tuzatilgan_savol',len(changes))
