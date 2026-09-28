import json,csv
from pathlib import Path
from collections import Counter
R=Path.cwd();O=R/'audit/production_3sinf';ledger=json.loads((O/'review_ledger.json').read_text(encoding='utf-8'));changes=json.loads((O/'changes_applied.json').read_text(encoding='utf-8'));status=json.loads((O/'NASHR_HOLATI.json').read_text(encoding='utf-8'))
status['changed_questions']=len({(x['file'],x['question_no']) for x in changes});status['review_statuses']=dict(Counter(x['status'] for x in ledger));status['blocking_reasons']=['Mavjud savollarning mazmuniy tekshiruvi hali yakunlanmagan'];status['user_requirements']={'minimum_questions_per_topic':None,'question_count_is_a_blocker':False,'missing_books_report_only':True,'priority':'Javob va mazmun to‘g‘riligi; har savolda faqat bitta to‘g‘ri javob','sources':'Faqat mahalliy kitoblar; internetdan qidirmaslik'}
for s in status['subjects']:s['holatlar']=dict(Counter(x['status'] for x in ledger if x['file'].split('/')[1]==s['fan']))
(O/'NASHR_HOLATI.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (O/'tekshiruv_navbati.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['file','question_no','sha256','status','evidence']);w.writeheader();w.writerows(x for x in ledger if x['status']!='joriy_tekshirildi')
body='''# Testlar sifati — joriy holat

Foydalanuvchining yangilangan talabi: **savollar soni kam bo‘lishi muammo emas; mavjud savollar va kalitlar to‘g‘ri bo‘lishi asosiy mezon.** Savollar soni yetishmasligi nashrni bloklamaydi. Testi yo‘q kitoblar alohida ro‘yxatda, ularga yangi savollar avtomatik qo‘shilmaydi. Manba — faqat mahalliy kitoblar papkasi.

## Tuzatishlar

- 3-sinf: **126 ta noyob savol tahrirlandi**. Bularning hammasi noto‘g‘ri kalit emas: tarjima, noaniq shart, bir nechta javob, tushunarsiz jumla va yetishmagan kontekst tuzatishlari ham shu songa kiradi.
- Ingliz tili 001–004 mavzularidagi **119 savol** matni, barcha variantlari va kaliti bilan tekshirildi; mahalliy PDFning 4–7-betlari ko‘rildi. 004-mavzu 29 savolligicha saqlandi.
- Matematikadagi **22 ta manbaga bog‘liq savol** mahalliy darslikning tegishli betlari bilan solishtirildi.
- 4-sinf: 50 000 + 4 000 + 3 000 savoli kaliti **57 000** ga tuzatildi; uzunlik masalasidagi aynan takror variant almashtirildi; Musiqadagi to‘rtta buzilgan yozuv tuzatildi.
- 6-sinf: 12 va 45 ni tub ko‘paytuvchilarga ajratish savollaridagi ikkinchi to‘g‘ri variantlar almashtirildi. Endi har birida bittadan to‘g‘ri javob bor.
- O‘zgargan JSON, TXT va jamlanmalar sinxronlashtirildi. Oldingi 85 ta mavzu/jamlanma nomuvofiqligi bartaraf etildi.

## Qayta tekshiruv

3–9-sinfdagi **101 647 savol** tuzilma nazoratidan qayta o‘tdi. Yaroqsiz javob indeksi, aynan takror variant, tekshiriladigan sodda arifmetik kalit xatosi yoki JSON/TXT/jamlanma nomuvofiqligi topilmadi. **Bu barcha savollar mazmunan xatosiz degani emas.** Son jihatdan teng variantlar kabi qoidalar faqat shubhali holatlarni topadi.

3-sinfdagi joriy mazmuniy tekshiruv: **307 savol**. Oldingi tekshiruv bilan mazmun izi mos 2339 savol bugun qayta o‘qilgan deb hisoblanmaydi. Qolgan savollar ham navbat bilan mahalliy darsliklarga solishtirilishi kerak.

**To‘liq sifat tekshiruvi tugamagan. Production tayyor deb belgilanmadi.** Kam savollilik bunga sabab emas; sabab — mavjud savollarning tekshiruvi hali tugamagan.

## Testi yo‘q kitoblar

- 3-sinf: Musiqa, Ona tili.
- 6-sinf: Musiqa, Tasviriy san’at.
- 7-sinf: Musiqa, Tasviriy san’at.
- 8-sinf: Chizmachilik.
- 10-sinf: mahalliy 16 ta kitobning hech biriga tayyor test topilmadi.
- 11-sinf: mahalliy 19 ta kitobning hech biriga tayyor test topilmadi.

Jami 42 kitob. To‘liq nomlar: TESTI_YOQ_KITOBLAR.md.

## Dalillar

- changes_applied.json — 3-sinfdagi oldin/keyin tahrirlar.
- ../production_known_fixes/changes.json — 4- va 6-sinfdagi 8 ta savol tahriri.
- review_ledger.json — savol darajasidagi mazmuniy tekshiruv izlari.
- local_source_reviews.json — mahalliy manba betlari va fayl izlari.
- ../production_known_fixes/recheck/statistika.json — barcha sinflarning eng so‘nggi avtomatik nazorati.
- tekshiruv_navbati.csv — joriy tasdiq olmagan savollar.

Keyingi ketma-ket ish: 3-sinf Ingliz tili 005-mavzudan davom etish. Shubhali kalitni taxminan to‘g‘ri deb belgilamaslik; manba bilan tekshirish yoki tasdiqsiz qoldirish.
'''
(O/'HISOBOT.md').write_text(body,encoding='utf-8')
(R/'3-sinf/HISOBOT.md').write_text('# 3-sinf — testlar sifati\n\n126 savol tahrirlandi, 307 savol joriy mazmuniy tekshiruvdan o‘tdi. Barcha savollar tekshiruvi tugamagan. Savollar soni kamligi xato hisoblanmaydi.\n\n[Batafsil holat](../audit/production_3sinf/HISOBOT.md)\n',encoding='utf-8')
p=O/'DAVOM_ETISH.md';old=p.read_text(encoding='utf-8');p.write_text('''# So‘nggi yangilanish — ustuvor

Foydalanuvchi savollar soni kam bo‘lishiga rozi. 30 ta/10+10+10 talabini nashr sharti qilmang, to‘ldirish bilan shug‘ullanmang. Asosiy maqsad mavjud savollarda xato qolmasligi va testi yo‘q kitoblar ro‘yxati. Faqat mahalliy kitoblar, internet yo‘q.

- 3-sinf tuzatishlar: 126 noyob savol; joriy mazmuniy tekshirilgan 307.
- Ingliz tili 004 ham tugadi: 29 savol saqlandi, 29 tasi tahrirlandi, PDF 7-bet ko‘rildi. Keyingi 005, PDF 8-bet.
- 4-sinf Matematika 003:19 kaliti; 008:23 takror varianti; Musiqa 001_Vatanimiz 1,7,11,22 yozuvlari; 6-sinf Matematika 003:11 va 14 ikkinchi to‘g‘ri variantlari tuzatildi. audit/production_known_fixes/changes.json.
- Barcha jamlanma nomuvofiqliklari sinxronlashtirildi. Oxirgi umumiy audit production_known_fixes/recheck da.
- NASHR_HOLATI da yagona blok: mavjud savollarning mazmuniy tekshiruvi tugamagan. Yetishmayotgan kitoblar va kam savol soni faqat ma’lumot.
- build_status.py eski snapshot asosida, qayta yugurtirmang; yangi review_ledger.json qaydlari va foydalanuvchi talablarini yo‘qotadi. Joriy hisobot va NASHR_HOLATI refresh_quality_status.py bilan yangilandi; undagi matn ham snapshot.

Quyidagi matn avvalgi holat, sonlar va navbat uchun yuqoridagini ustun oling.

'''+old,encoding='utf-8')
print('Quality-first status updated:',status['changed_questions'],status['review_statuses'])
