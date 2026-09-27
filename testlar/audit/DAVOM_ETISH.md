# Davom ettirish holati

Foydalanuvchi 3–9-sinflardagi HAR BIR savolni birma-bir tekshirib, shundan keyin hisobot berishni so‘ragan. Bu topshiriq HALI YAKUNLANMAGAN. Avtomatik tekshiruvni mazmuniy tekshiruv o‘rniga ko‘rsatmaslik kerak. Asl testlar o‘zgartirilmagan.

- 83 312 ta alohida mavzu savoli bor.
- 3-sinf Matematika: 001–083 fayllarning barcha 2 477 savoli o‘qilgan.
- 3-sinf Musiqa: 001_Ye.json dagi 30 savol o‘qilgan.
- Boshqa sinf/fanlarda avtomatik topilgan 21 savol alohida o‘qilgan.
- 3-sinf Odobnoma: 001–006 fayllarning barcha 180 ta savoli o‘qilgan.
- Jami mazmunan ko‘rilgan: 2 708. Qolgan: 80 604.
- 20 ta ko‘rilgan savolga darslik/rasm yoki manba kerak. Ular tasdiqlangan hisoblanmaydi.

Keyingi ketma-ket bosqich: 3-sinf Odobnoma, 007-mavzudan. Keyin O‘qish, Rus tili, Tabiatshunoslik, Tarbiya, Tasviriy san’at, Texnologiya; so‘ng 4–9-sinflar. Ingliz tili va Ona tili 3-sinf papkalarida alohida test JSON yo‘q.

## Dalillar va holat

- `manual_reviews.json`: faqat matni, 4 varianti va kaliti haqiqatda o‘qilgan savollar. Har biri asl savolning SHA-256 izi bilan bog‘langan.
- `savollar_holati.jsonl`: 83 312 savolning individual holati. `semantic_status=tekshirilmagan` qaydlari hali o‘qilmagan.
- `MAZMUNIY_TOPILMALAR.md`: Yangilanadigan topilmalar, fayl/savol raqami, asl variantlar va izohlar.
- `ORALIQ_HISOBOT.md`: ishning to‘liq tugamaganini aniq ko‘rsatadigan oraliq hisobot.

## Keyingi tekshiruv tartibi

1. Mavzu fayllarini kichik, kesilmaydigan partiyalarda o‘qish. Har bir savolning barcha variantlari va kalitini ko‘rish. Tool chiqishi kesilsa, yetishmagan qismini qayta o‘qish.
2. Faqat o‘qilgan savollarni `manual_reviews.json` ga yozish. Avtomatik qoida yoki namunaviy ko‘rish asosida butun faylni mazmunan ko‘rildi deb belgilamaslik.
3. Noaniq faktlarni ishonchli manbadan tekshirish; manbasiz hikoya, rasm va jadval savollarini `manba_kerak` qilib saqlash.
4. Topilgan xatolarni tuzatish takliflari bilan qayd etish; foydalanuvchi so‘ramaguncha asl testlarga tahrir kiritmaslik.
5. `python3 audit/tekshir.py`, keyin `python3 audit/report.py` hisobotlarni qayta yaratadi. Birinchisi mavjud qo‘lda ko‘rilgan savollarning izlarini tekshiradi.

`record_batch.py` faqat Matematika 3-sinf uchun yozilgan. Uni boshqa fanlarni ko‘rildi deb belgilash uchun ishlatmaslik kerak.

## Avtomatik tekshiruvda hisobga olingan muhim holatlar

- Genetikada AA, Aa, aa turli variantlar. Formulada R/r va r/R bir xil emas. Kod chiqishida bo‘sh joylar muhim. Shuning uchun takrorlar aniqlashda harf registri yoki ichki bo‘sh joylar normallashtirilmaydi.
- TXT dagi raqamli mavzu sarlavhalari savol emas; ko‘p qatorli savollar to‘liq taqqoslanadi. Dastlab ko‘ringan nusxa farqlari parserdan chiqqan, haqiqiy TXT/JSON farqi qolmadi.
- Kasrga bo‘lishda slash bilan yozilgan kasrlar butun operand sifatida olinadi: 1/2 ÷ 1/2 = 1.
- Teng qiymatli ifoda/oddiy kasrlar avtomatik signal, lekin savol aynan yozilish shaklini so‘rasa bu xato bo‘lmasligi mumkin.
- Belgilar buzilishi detektori gumon bildiradi; barcha 616 signal tasdiqlangan imlo xatosi emas.

To‘liq audit bitmaguncha yakuniy deb nomlamaslik, bajarilmagan ishni bajarildi deb aytmaslik va ish fonda davom etadi deb va’da bermaslik kerak.

Odobnoma 001–006 savollari uchun 2019-yilgi darslikning 5–32-betlari bilan solishtirildi: https://uzedu.online/books/479/479-9d57c.pdf . Bu darslikka moslikni tekshirishdir, rivoyatlarni mustaqil tarixiy fakt sifatida tasdiqlash emas. Alohida qaydlar odobnoma_notes_1_3.json va odobnoma_notes_4_6.json da.
