# Testlar sifati — joriy holat

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
