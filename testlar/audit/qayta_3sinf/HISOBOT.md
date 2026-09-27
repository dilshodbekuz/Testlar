# 3-sinf: tuzatishlarni qayta tekshirish — 2026-09-27

**Xulosa: barcha fanlar to‘liq to‘g‘rilangan deb bo‘lmaydi.**

Qamrov: faqat 3-sinfning 11 fan papkasi. 9 fanda 530 ta alohida mavzu JSON fayli va 15 778 ta savol bor. Musiqa va Ona tilida alohida testlar yo‘q. Savollar soni jamlanma va TXT nusxalarini qayta sanamaydi; turli mavzu fayllaridagi takrorlar alohida sanalgan.

Bu tekshiruv barcha fayllarning tuzilishi, TXT/JSON mosligi, jamlanmalar tarkibi, tuzatishlar jurnali va oldingi topilmalarning amaldagi holatini qamrab oladi. Har bir 15 778 savolning mazmuni boshidan oxirigacha qayta o‘qilgani yoki darslik bilan tasdiqlangani da’vo qilinmaydi. Har bir mavjud fanda tanlangan savollar mazmunan ham ko‘rildi.

## Fanlar kesimi

| Fan | Mavzu fayli | Savol | Jurnaldagi alohida savol | Hozirgi topilma |
|---|---:|---:|---:|---|
| Ingliz tili | 67 | 1998 | 87 | 001:3 — «singililar»; 001:8 — «ukalari» shakli; til tahriri qolgan. |
| Matematika | 83 | 2477 | 99 | 013:5 va 033:1 — namuna/xona qo‘shiluvchilari sharti yetishmaydi. |
| Musiqa | 0 | 0 | 0 | Papka bo‘sh, tekshiriladigan test yo‘q. |
| Odobnoma | 24 | 716 | 255 | 002:4 va 002:25 — savol va javoblarda buzilgan matn qolgan. |
| Ona tili | 0 | 0 | 0 | Alohida mavzu testlari yo‘q. |
| O‘qish | 164 | 4865 | 26 | 559 savolda g‘ayrioddiy belgi signali; jamlanma to‘liq emas. |
| Rus tili | 24 | 717 | 119 | 001:2 — «O‘quvchisidir», 001:9 — «Shkolning direktyori»; til tahriri kerak. |
| Tabiatshunoslik | 72 | 2148 | 728 | 001:6 — «Cho‘lla»; jamlanmada 31 fayl yetishmaydi. |
| Tarbiya | 21 | 621 | 261 | 001:5 mazmunsiz kalit; 001:6 inkor shakli mos emas; jamlanma to‘liq emas. |
| Tasviriy san’at | 45 | 1340 | 514 | 001:7 aylana ta’rif, 001:10 grammatik buzilgan kalit; jamlanma to‘liq emas. |
| Texnologiya | 30 | 896 | 346 | 001:8 — «Detalllarni», 001:9 — «Rang tutirib»; til tahriri kerak. |

## Qo‘llangan tuzatishlar

Jurnalda 3-sinfga oid 2471 yozuv, 2435 ta alohida savol bor. Har bir savol uchun jurnalning eng so‘nggi `yangi` qiymati amaldagi JSON bilan aynan mos. Bu sonlar mustaqil tasdiqlangan xatolar soni emas; jurnalda takroriy va o‘zgarishsiz yozuvlar ham bor.

Oldingi aniq xatolardan Matematika 073:15 (32 kun oldin — shanba), 024:17 va 024:25 (uchburchak tomonlari) amalda to‘g‘ri tuzatilgan.

## Avtomatik tekshiruv natijasi

- JSON ochilishi, 4 ta bo‘sh bo‘lmagan variant, 0–3 oralig‘idagi javob indeksi va qiyinlik qiymatlarida xato aniqlanmadi.
- Barcha 530 mavzuning TXT nusxalari JSON savol, variant va kalitlariga mos.
- Aynan bir xil variantlar topilmadi. Oddiy arifmetik shablonga mos 578 savol hisoblandi; ularda noto‘g‘ri kalit signali yo‘q. Bu barcha matematik masalalar tekshirildi degani emas.
- 13 ta teng son qiymatli variant signali ko‘rildi. Aksariyati noto‘g‘ri variantlarning tengligi yoki savol yozilish shaklini so‘ragani sababli xato emas. 013:5 va 033:1 da yetishmayotgan kontekst bor.
- O‘qishda 559 savolda g‘ayrioddiy belgi bor. Bu 559 ta noto‘g‘ri javob degani emas; matnni tahrirlash signali. «Vàtàn», «Undà bilim o‘chîg‘i» kabi buzilishlar amalda mavjud.

## Jamlanma kamchiliklari

| Fan | `_TOLIQ.json`da yo‘q alohida fayl | Ulardagi savol |
|---|---:|---:|
| O‘qish | 87 | 2574 |
| Tabiatshunoslik | 31 | 926 |
| Tarbiya | 1 | 29 |
| Tasviriy san’at | 17 | 506 |

Jami 136 ta alohida faylning 4 035 savoli jamlanmalarda yetishmaydi. Jamlanmadan test yuklaydigan tizim bu fayllarni olmaydi. 124 ta mavzu raqami bir papkada bir nechta faylda ishlatilgan; bular avtomatik o‘chiriladigan dublikatlar deb hisoblanmadi.

## Aniq misollar va tavsiya

### Matematika, 013_Yig'indini songa bo'lish.json, 5-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Matematika/013_Yig'indini songa bo'lish.json>)

Namunada 86 : 2 ni hisoblash uchun 86 soni qanday yoyilgan?

- A) 70 + 16
- B) 90 − 4
- C) 60 + 26
- D) 80 + 6 **(kalit)**

Namuna berilmagan. 70+16, 60+26, 80+6 ham 86 ga teng. «86 soni xona qo‘shiluvchilariga qanday ajratiladi?» deb aniqlashtirish kerak.

### Matematika, 033_Ikki xonali songa ko'paytirish.json, 1-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Matematika/033_Ikki xonali songa ko'paytirish.json>)

12 · 15 ko'paytmasini yechishda 15 soni qanday yoyildi?

- A) 15 + 0
- B) 10 · 5
- C) 10 + 5 **(kalit)**
- D) 12 + 3

15+0, 10+5, 12+3 ham 15 ga teng. Xona qo‘shiluvchilari sharti yoki namuna zarur.

### Odobnoma, 002_Davlat ramzlari — milliy iftixorimiz.json, 4-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Odobnoma/002_Davlat ramzlari — milliy iftixorimiz.json>)

Bayroq nekning ramzi?

- A) Ozodlik va tinchliq **(kalit)**
- B) Qator va yalpi
- C) Bilim va amaliyot
- D) Bog' va maydonlar

«nekning» → «nimaning», «tinchliq» → «tinchlik»; ma’nosiz variantlar qayta tuzilsin.

### Odobnoma, 002_Davlat ramzlari — milliy iftixorimiz.json, 25-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Odobnoma/002_Davlat ramzlari — milliy iftixorimiz.json>)

Nega davlat madhiyasini yangraganda faqat iftixor emasmi, boshqa tuyg'ular ham uyg'onadi?

- A) Madhiya rang'in
- B) Madhiya qora
- C) Madhiya buydoq
- D) Madhiya vatanimizning tarixini va azamini ta'minlaydi **(kalit)**

Savol va barcha variantlar mazmunli shaklda qayta yozilishi kerak.

### Tarbiya, 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json, 5-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json>)

O'ng qo'l qoidasi qayerda ishlatiladi?

- A) Yo'lda faqat
- B) Faqat oshxonada
- C) Faqat o'yinda
- D) Muhim damda, o'zgarlik ko'rsatishda **(kalit)**

«Muhim damda, o‘zgarlik ko‘rsatishda» savolga tushunarli javob bermaydi. Darslik konteksti bilan qayta tuzish kerak.

### Tarbiya, 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json, 6-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json>)

Tanaffusda nima qilmaslik kerak?

- A) Yuguraslik
- B) Kitob o'qish
- C) Kechiroq kelish
- D) Boshqalarning dam olishiga xalaqit qilmaslik **(kalit)**

«Nima qilmaslik kerak?» savoliga «xalaqit qilmaslik» javobi ikki inkor hosil qiladi. Savol «Tanaffusda qanday qoidaga amal qilish kerak?» deb yozilsin.

### Tarbiya, 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json, 8-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json>)

Xavfsizlik qoidalariga rioya qilish nima uchun zarur?

- A) Jarohalarishlashning oldini olish **(kalit)**
- B) Vaqt o'tkazish
- C) O'qituvchini xursand qilish
- D) Faqat qoidaga amal qilish

«Jarohalarishlashning» → «Jarohatlanishning».

### Ingliz tili, 001_Unit 1 Lesson 1 I have two sisters.json, 3-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Ingliz tili/001_Unit 1 Lesson 1 I have two sisters.json>)

Sisters so'zi nima anglatadi?

- A) Togalar
- B) Onalar
- C) Akalar yoki ukalari
- D) Opalar yoki singililar **(kalit)**

«Opalar yoki singililar» → «Opalar yoki singillar».

### Rus tili, 001_В школе.json, 2-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json>)

Feruza kimdir?

- A) Direktyordir
- B) O'quvchisidir **(kalit)**
- C) Klassnyy rukovoditeldir
- D) O'qituvchidir

«Feruza kimdir?» → «Feruza kim?»; «O‘quvchisidir» → «O‘quvchi».

### O‘qish, 005_Bîr ûchôk suv halos ekanmi.json, 8-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf O‘qish/005_Bîr ûchôk suv halos ekanmi.json>)

Sirdarya Qoradarya daryosi bilan qanday bog'lanadi?

- A) Ajraladi
- B) Birlashadi **(kalit)**
- C) O'tadi
- D) Biroz chuqurga tushadi

«bilalar», «Ko‘zbiyallag‘ich, båkinmachiq va siqqa» buzilgan. O‘yin nomlarini asl matn bilan solishtirib tiklash kerak.

### Tabiatshunoslik, 001_Tabiatshunoslik nimani o'rganadi.json, 6-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tabiatshunoslik/001_Tabiatshunoslik nimani o'rganadi.json>)

Qor, muz va yomg'ir suvlaridan nima hosil bo'ladi?

- A) Dengizlar
- B) Cho'lla
- C) Bulutlar
- D) Daryolar **(kalit)**

«Cho‘lla» variantini «Cho‘llar» deb tahrirlash kerak.

### Tasviriy san’at, 001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json, 7-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json>)

Rasm ishlashda to'g'ri o'tirish qanday bo'lishi kerak?

- A) To'g'ri **(kalit)**
- B) Orqaga yastanib
- C) Burilgan
- D) Yotib

«To‘g‘ri o‘tirish qanday? — To‘g‘ri» bilimni tekshirmaydigan aylana javob. Holat aniq tasvirlansin.

### Tasviriy san’at, 001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json, 10-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json>)

San'at ustalari nima qiladi?

- A) Rasm, haykal, relyef va boshqa san'at asarlarini tuza va ishlaydigan **(kalit)**
- B) Faqat sport o'rgatadigan
- C) Faqat haykal yasaydigan
- D) Faqat rasm ishlaydigan

Kalitdagi «tuza va ishlaydigan» grammatik buzilgan; «San’at asarlarini yaratadi» shakli mos.

### Texnologiya, 001_«Kuz» manzarasini applikatsiya usulida yasash.json, 8-savol

[Asl fayl](</Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/3-sinf 3-Sinf Texnologiya/001_«Kuz» manzarasini applikatsiya usulida yasash.json>)

Applikatsiya yasashda qaysi qadamdan boshlanadi?

- A) Rang tanlashdan
- B) O'lchashdan
- C) Yelimlashdan
- D) Detalllarni tayyorlashdan **(kalit)**

«Detalllarni» → «Detallarni»; savolni «Applikatsiya yasash qaysi bosqichdan boshlanadi?» deb yozish kerak.

## Eski topilmalar holati

Oldingi izohli qaydlarning 181 tasi aynan o‘zgarishsiz qolgan: 158 ta tahrir qaydi, 15 ta manba kerak qaydi va 8 ta ijobiy tekshiruv izohi. Shuning uchun 181 sonini xatolar soni deb talqin qilish mumkin emas. Yana 111 ta izohli savol o‘zgargan; o‘zgargani o‘z-o‘zidan to‘liq to‘g‘ri bo‘lganini bildirmaydi. Musiqadagi avvalgi 30 savol fayli hozir mavjud emas.

[Oldingi qaydlar bilan to‘liq taqqoslash](old_issues.json).

Asl test fayllari bu tekshiruvda o‘zgartirilmadi. 4–9-sinflar tekshirilmadi.
