# Tekshiruvni davom ettirish (2026-09-27 holati)
Limit tugab barcha agentlar to'xtadi. Keyingi safar KO'PI BILAN 2-3 agent parallel (sonnet), sinfma-sinf.
Qo'llanma: QOLLANMA.md. Tuzatishlar jurnali: ../tuzatishlar_qolda.jsonl. Har agent holati: ish/<ID>/tayyor.txt.

## 3-sinf — TO'LIQ TEKSHIRILDI (audit tugadi)
- Barcha kitoblar tekshirildi: Matematika, Odobnoma, Rus tili, Tarbiya, Texnologiya, Tasviriy san'at,
  Tabiatshunoslik, O'qish (1-82 a/b), Ingliz tili (1-67).
- 2026-09-27: Ingliz tili 48-67 tekshirildi (men, agentsiz), 2 ta xato tuzatildi (50:29, 53:15).
- Eslatma: Musiqa va Ona tili kitoblari hali generatsiya qilinmagan (test_generator.py orqali),
  audit ro'yxatida yo'q — generatsiyadan keyin tekshiriladi.
## 4-sinf — TO'LIQ TEKSHIRILDI (audit tugadi, 2026-09-27, men agentsiz)
- Barcha 11 ta kitob (~324 mavzu, ~9700 savol) 100% tekshirildi: Matematika, Musiqa, Odobnoma,
  Ona tili, O'qish, O'qish (metodika), Rus tili, Tabiatshunoslik, Tasviriy san'at, Texnologiya, Ingliz tili.
- Jami 24 ta xato topib tuzatildi: Matematika 14, Texnologiya 5, Ingliz tili 3, Tabiatshunoslik 1.
- Musiqa, Odobnoma, Ona tili, O'qish, O'qish metodika, Rus tili, Tasviriy san'at — xato topilmadi.
- Batafsil: ish/men/tayyor.txt.
## 5-sinf — TO'LIQ TEKSHIRILDI (audit tugadi, 2026-09-27, men agentsiz)
- Barcha 13 ta kitob 100% tekshirildi: Vatan tuyg'usi, Tasviriy san'at, Ingliz tili, Biologiya, Adabiyot,
  Geografiya, Informatika, Matematika (1 va 2-qism), Musiqa, Ona tili, Rus tili, Tarixdan hikoyalar, Texnologiya.
- Jami 19 ta xato topib tuzatildi: Geografiya 4, Informatika 5, Matematika 1-qism 4, Matematika 2-qism 4,
  Musiqa 2, Rus tili 4 (jumladan yosh-hisob masalasida savol matni xatosi va "sessenta" so'z buzilishi).
- Vatan tuyg'usi, Tasviriy san'at, Ingliz tili, Biologiya, Adabiyot, Ona tili, Tarixdan hikoyalar, Texnologiya — xato topilmadi.
- 2 ta joy manbasiz/chalkash bo'lgani uchun tuzatilmay qoldirildi (Matematika 1-qism 14:27, Matematika 2-qism 20:29).
- Batafsil: ish/men/tayyor.txt.
## 6-sinf — QISMAN (2026-09-27, men agentsiz)
- Avtomatik skan (HISOBOT.md) va qo'lda tasdiqlangan CSV'lardagi (TASDIQLANGAN_MUAMMOLAR,
  QOLDA_TASDIQLANGAN_MUAMMOLAR, TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR, TASDIQLANGAN_ALOHIDA_KIRILL)
  barcha haqiqiy xatolar tekshirildi va tuzatildi: Matematika 011:19, 013:1, 014:23; Geografiya 003:19,
  006-mavzu (10 ta "gipoteza" so'zi); Rus tili 007:12; Rus tili 008-mavzu (30 savol, butunlay kirillcha
  edi — lotin yozuviga o'tkazildi); Ona tili 035:10. Qolgan CSV qatorlarining aksariyati avvalgi
  sessiyada allaqachon tuzatilgan ekan (fayl tekshirilib tasdiqlandi).
- Ingliz tili'dagi 2 ta "ziddiyatli takror" guruhi (004/010, 058/059) tekshirildi — turli matn/kontekstga
  tegishli bo'lgani uchun xato emas deb topildi, tegilmadi.
- TUZATILMAGAN: Botanika, Fizika, Informatika, Informatika(1), Informatika(2), Adabiyot(1,2), Musiqa,
  Tasviriy san'at, Ingliz tili, Tarix — mexanik skanda signal chiqmagan, lekin mazmun jihatdan
  savolma-savol hali o'qib chiqilmagan (~9000+ savol qoldi). Keyingi qadam: shu kitoblarni navbat
  bilan qo'lda o'qib chiqish.
## 7-9-sinf: qisman holatlar ish/A20../tayyor.txt da; qolganlari navbat.txt da (A21-A41). Keyingi: 6-sinf qolgan kitoblari, keyin 7-sinf.
