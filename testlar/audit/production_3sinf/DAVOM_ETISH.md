# So‘nggi yangilanish — ustuvor

Foydalanuvchi savollar soni kam bo‘lishiga rozi. 30 ta/10+10+10 talabini nashr sharti qilmang, to‘ldirish bilan shug‘ullanmang. Asosiy maqsad mavjud savollarda xato qolmasligi va testi yo‘q kitoblar ro‘yxati. Faqat mahalliy kitoblar, internet yo‘q.

- 3-sinf tuzatishlar: 126 noyob savol; joriy mazmuniy tekshirilgan 307.
- Ingliz tili 004 ham tugadi: 29 savol saqlandi, 29 tasi tahrirlandi, PDF 7-bet ko‘rildi. Keyingi 005, PDF 8-bet.
- 4-sinf Matematika 003:19 kaliti; 008:23 takror varianti; Musiqa 001_Vatanimiz 1,7,11,22 yozuvlari; 6-sinf Matematika 003:11 va 14 ikkinchi to‘g‘ri variantlari tuzatildi. audit/production_known_fixes/changes.json.
- Barcha jamlanma nomuvofiqliklari sinxronlashtirildi. Oxirgi umumiy audit production_known_fixes/recheck da.
- NASHR_HOLATI da yagona blok: mavjud savollarning mazmuniy tekshiruvi tugamagan. Yetishmayotgan kitoblar va kam savol soni faqat ma’lumot.
- build_status.py eski snapshot asosida, qayta yugurtirmang; yangi review_ledger.json qaydlari va foydalanuvchi talablarini yo‘qotadi. Joriy hisobot va NASHR_HOLATI refresh_quality_status.py bilan yangilandi; undagi matn ham snapshot.

Quyidagi matn avvalgi holat, sonlar va navbat uchun yuqoridagini ustun oling.

# Joriy ishni davom ettirish

Foydalanuvchi barcha testlarni tuzatib productionga tayyorlashni, 3-sinfdan boshlashni va testi yo‘q kitoblarni aytishni so‘ragan. Ish HALI tugamagan. Foydalanuvchining so‘nggi ko‘rsatmasi: internetdan qidirmang; manbalar ../kitoblar ichida.

- ../kitoblar/3-sinf: 11 PDF; Ingliz tili, Ona tili, Musiqa skan sahifalar. pdftoppm bilan ko‘rish ishlaydi. PDFlar foydalanuvchidan qayta so‘ralmasin.
- Barcha sinflar bo‘yicha 42 PDF uchun tayyor mavzu testlari yo‘q. TESTI_YOQ_KITOBLAR.md ga qarang. 3-sinfda Ona tili va Musiqa.
- 3-sinf: 570 mavzu, 16 963 savol. 97 noyob savol o‘zgartirildi, oldin/keyin changes_applied.json da. Asl nusxalar backup da.
- Ingliz tili 001–003: 90 savol to‘liq ko‘rildi, 73 tahrir; mahalliy PDF 4–6-betlari ham ko‘rildi. Keyingi mavzu 004, PDF 7-bet.
- Matematika: oldingi tahrirlangan va shubhali savollar o‘qildi; 24 savol tahrirlandi. 22 manba signali mahalliy 2019-yilgi PDF bilan tekshirildi, local_source_reviews.json da aniq betlar va sha256 saqlangan.
- Joriy tekshirilgan: 278. Oldingi hash-mos qaydlar: 2339 (bugun qayta tekshirildi demang). 14 346 savolning mazmuni joriy tasdiqsiz.
- 123 mavzuda jami 137 savol kam: completeness.json. Yangi savol qo‘shilganda avvalgi question_no indekslari siljimasligi uchun audit izlari yangilansin.
- JSON/TXT/_TOLIQ mos. Yangi _testlar_index.json fayllari noyob identifikatorlar bilan qo‘shildi. Asl _mavzular.json kitob betlarini saqlaydi; 159 takror mavzu-raqami guruhi bor, ularni manba asosida ajratish kerak.
- Audit/production_3sinf/local_sources ichida 11 kitobning sahifama-sahifa ajratilgan matni JSON ko‘rinishida, skan kitoblar uchun bo‘sh bo‘lishi tabiiy.
- 4–9-sinfdagi oldingi topilgan xatolar hali bu bosqichda tuzatilmagan (publish_2026_09_28 hisobotiga qarang).
- Python: C:/Users/xakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe (har doim -X utf8). pypdf bor, fitz yo‘q.
- Poppler: C:/Users/xakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe.
- sync.py qayta sinxronlaydi, recheck.py avtomatik audit, validate.py izlar va jamlanmani tekshiradi; --production tasdiqsiz to‘plamni rad qiladi.
- fix_questions.py va fix_followup.py bir martalik tahrir tarixidir: qayta yugurtirib keyingi tahrirlarni bekor qilmang.
- build_status.py joriy qaydlarni avvalgi snapshotdan yig‘adi: yangi qo‘lda tekshiruvlar qo‘shilgach yangilamasdan yugurtirmang. Yakuniy hisobotdagi qo‘shimcha to‘liqlik bo‘limi alohida yangilangan.

To‘liq tekshiruv tugamaguncha production_ready false bo‘lsin. Manbalar yo‘q deb to‘xtamang; hammasi mahalliy kitoblar papkasida. Internetdan foydalanmang.
