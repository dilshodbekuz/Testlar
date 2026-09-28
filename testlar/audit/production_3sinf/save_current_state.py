import json
from pathlib import Path
O=Path('audit/production_3sinf');p=O/'HISOBOT.md';s=p.read_text(encoding='utf-8');s+='\n## Savollar sonining to‘liqligi\n\nLoyihadagi 30 savol (10 oson, 10 o‘rtacha, 10 qiyin) talabiga nisbatan 123 ta mavzu to‘liq emas, jami 137 savol yetishmaydi. Mavjud savollar o‘chirilmadi. Batafsil ro‘yxat: completeness.json.\n'
p.write_text(s,encoding='utf-8')
p=O/'NASHR_HOLATI.json';d=json.loads(p.read_text(encoding='utf-8'));d['incomplete_topics']=123;d['missing_question_slots']=137;d['blocking_reasons'].append('123 mavzuda 30 savollik to‘plam to‘liq emas');d['local_books_directory']=str(Path.cwd().parent/'kitoblar');d['internet_allowed']=False;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(O/'DAVOM_ETISH.md').write_text('''# Joriy ishni davom ettirish

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
''',encoding='utf-8')
print('Local-source status and continuation records saved.')
