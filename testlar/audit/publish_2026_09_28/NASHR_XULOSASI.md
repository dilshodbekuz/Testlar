# Nashr oldidan qayta tekshiruv — 2026-09-28

**Xulosa: hozirgi holatda to‘liq tayyor test banki sifatida nashr qilish tavsiya etilmaydi.**

3–9-sinflarning barcha alohida mavzu JSON fayllari avtomatik tekshirildi. Shubhali signallar va har bir sinfdan tanlangan savollar mazmunan ko‘rildi. Barcha savollar birma-bir darslik bilan solishtirilgani yoki xatosizligi tasdiqlangani yo‘q. Test fayllari o‘zgartirilmadi; ushbu tekshiruv natijalari alohida saqlandi.

| Sinf | Mavzu fayli | Savol | Qayta hisoblangan arifmetik savol | Manbaga ishora signali* |
|---|---:|---:|---:|---:|
| 3-sinf | 570 | 16963 | 578 | 1106 |
| 4-sinf | 419 | 12484 | 99 | 676 |
| 5-sinf | 390 | 11610 | 44 | 512 |
| 6-sinf | 433 | 12898 | 54 | 826 |
| 7-sinf | 501 | 14610 | 8 | 851 |
| 8-sinf | 487 | 14477 | 0 | 1477 |
| 9-sinf | 623 | 18605 | 7 | 1563 |

Jami: **3423 mavzu, 101647 savol**. Arifmetik shablon bilan 790 savol qayta hisoblandi.

*Manbaga ishora — matn, rasm, she’r yoki jadval kabi so‘zlar bo‘yicha avtomatik signal; ularning barchasi xato yoki manbasiz degani emas.

## Tasdiqlangan muammolar

### 1. 4-sinf/4-sinf 4-Sinf Matematika/003_Ko'p xonali sonlarni qo'shish.json — 19-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Matematika/003_Ko'p xonali sonlarni qo'shish.json:205>)

Hisoblang: 50000 + 4000 + 3000 = ?

A) 55000 | B) 56000 | C) 57000 | D) 58000

Belgilangan javob: B

Kalit xato: 50000 + 4000 + 3000 = 57000. B (56000) belgilangan.

**Tavsiya:** Kalitni C (indeks 2) ga almashtirish.

### 2. 4-sinf/4-sinf 4-Sinf Matematika/008_Uzunlik birliklari.json — 23-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Matematika/008_Uzunlik birliklari.json:249>)

118 m 06 cm – 92 m 32 cm nechaga teng?

A) 26 m 74 cm | B) 26 m 74 cm | C) 25 m 74 cm | D) 25 m 75 cm

Belgilangan javob: C

A va B variantlari aynan bir xil: 26 m 74 cm. To‘g‘ri javob C (25 m 74 cm).

**Tavsiya:** Takror noto‘g‘ri variantlardan birini boshqa qiymat bilan almashtirish.

### 3. 6-sinf/6-sinf 6-Sinf Matematika/003_Sonning tub ko'paytuvchilarga yoyilmasi.json — 11-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/6-sinf/6-sinf 6-Sinf Matematika/003_Sonning tub ko'paytuvchilarga yoyilmasi.json:117>)

12 sonini tub ko'paytuvchilarga yoying

A) 2 × 6 | B) 3 × 4 | C) 2 × 3 × 2 | D) 2² × 3

Belgilangan javob: D

C: 2 × 3 × 2 va D: 2² × 3 — ikkalasi ham 12 ning tub ko‘paytuvchilarga yoyilmasi. Savol darajali yozuvni talab qilmagan.

**Tavsiya:** Savolda darajalar yordamida yozishni aniq talab qilish yoki C variantini almashtirish.

### 4. 6-sinf/6-sinf 6-Sinf Matematika/003_Sonning tub ko'paytuvchilarga yoyilmasi.json — 14-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/6-sinf/6-sinf 6-Sinf Matematika/003_Sonning tub ko'paytuvchilarga yoyilmasi.json:150>)

45 ni tub ko'paytuvchilarga yoying

A) 3 × 3 × 5 | B) 3² × 5 | C) 5 × 9 | D) 3 × 15

Belgilangan javob: B

A: 3 × 3 × 5 va B: 3² × 5 — ikkalasi ham 45 ning tub ko‘paytuvchilarga yoyilmasi.

**Tavsiya:** Savolda darajalar yordamida yozishni aniq talab qilish yoki A variantini almashtirish.

### 5. 3-sinf/3-sinf 3-Sinf Ingliz tili/003_Unit 1 Lesson 3 Are you a driver.json — 2-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/3-sinf/3-sinf 3-Sinf Ingliz tili/003_Unit 1 Lesson 3 Are you a driver.json:18>)

Quyidagi kasblardan qaysi biri matnda nomlanmaydi?

A) Doktor | B) Voqea | C) Muhandis | D) O'qituvchi

Belgilangan javob: C

Savol matnga tayanadi, lekin JSON ichida manba matni yo‘q. Kasblar orasiga “Voqea” kiritilgan.

**Tavsiya:** Asl matnni biriktirish, variantlarni mazmunan qayta tuzish.

### 6. 4-sinf/4-sinf 4-Sinf Ingliz tili/010_Unit 3 - Lesson 1 Do you help your mum.json — 26-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Ingliz tili/010_Unit 3 - Lesson 1 Do you help your mum.json:282>)

Agar haftalik jadvalda ko'rsatilgan barcha 5 ta harakatni bajaradigan bo'lsan, nechta kunni to'liq yurakda ish qilish kerak?

A) 7 ta kun | B) 3 ta kun | C) har bir kun | D) 5 ta kun

Belgilangan javob: D

“nechta kunni to‘liq yurakda ish qilish kerak” jumlasi tushunarsiz; beshta harakatdan beshta kun degan javob kelib chiqmaydi. Jadval ilova qilinmagan.

**Tavsiya:** Jadvalni qo‘shish va savolni aniq qayta yozish.

### 7. 5-sinf/5-sinf 5-Sinf Adabiyot/001_Adabiyot – so'z san'ati.json — 26-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/5-sinf/5-sinf 5-Sinf Adabiyot/001_Adabiyot – so'z san'ati.json:282>)

Quyidagi jumla matndagi qaysi tushunchani eng yaxshi ifoda etadi: "Bolalar loy-kulgacha, qumdan uy, plastilində qushcha yasay ekan, yodiga o'sha narsalarning surati keltiradi"

A) Bolalar faqat o'yn yasadi | B) Bolalarning qo'li chala bo'lgani uchun | C) Bolalarning xayoli noto'g'ri bo'lgani uchun | D) Bolalarning obrazli fikrlash qobiliyati va xayol kuchining rivojlanishini

Belgilangan javob: D

Iqtibos va variantlar grammatik jihatdan buzilgan: “loy-kulgacha”, “plastilində”, “yasay ekan”, “Bolalar faqat o‘yn yasadi”.

**Tavsiya:** Asl parcha bilan taqqoslab qayta tahrirlash.

### 8. 6-sinf/6-sinf 6-Sinf Adabiyot (2-qism)/001_Said Ahmad.json — 20-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/6-sinf/6-sinf 6-Sinf Adabiyot (2-qism)/001_Said Ahmad.json:216>)

Paxtakorning rasmini gazeta birinchi betida chap-chunkur holati qanday tasvirlanadilar?

A) O'tirib qo'q | B) Yutib o'yin | C) Yurmasin turib | D) Paxta qistirib kulib

Belgilangan javob: D

Savol va chalg‘ituvchi variantlar tushunarsiz: “chap-chunkur”, “O‘tirib qo‘q”, “Yutib o‘yin”.

**Tavsiya:** Asl hikoya asosida savol va barcha variantlarni qayta yozish.

### 9. 4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json — 1-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json:7>)

Band shakli nechta shå'riy misradan iborat?

A) 4 ta | B) 5 ta | C) 3 ta | D) 6 ta

Belgilangan javob: A

“shå’riy”/“Shå’riy” ko‘rinishidagi buzilgan yozuv mavjud.

**Tavsiya:** “she’riy”/“She’riy” ko‘rinishiga tuzatish.

### 10. 4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json — 7-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json:73>)

Band shakli nimalardan tarkib topadi?

A) Naqarot va ilhomdan | B) Musiqa asboblaridan | C) Raqs va oyinlardan | D) Shå'riy misra va kuydan

Belgilangan javob: D

“shå’riy”/“Shå’riy” ko‘rinishidagi buzilgan yozuv mavjud.

**Tavsiya:** “she’riy”/“She’riy” ko‘rinishiga tuzatish.

### 11. 4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json — 11-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json:117>)

Band va naqarotli band shakl o'rtasida asosiy farq nima?

A) Kattalikda farq | B) Janri boshqacha | C) Kuylari boshqacha | D) Naqarotli band shaklida shå'riy misralar o'zgaruvchan, naqarot o'zgarmasdan takrorlanadi

Belgilangan javob: D

“shå’riy”/“Shå’riy” ko‘rinishidagi buzilgan yozuv mavjud.

**Tavsiya:** “she’riy”/“She’riy” ko‘rinishiga tuzatish.

### 12. 4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json — 22-savol

[Faylni ochish](<C:/Users/xakim/OneDrive/Desktop/Test_Generator/testlar/4-sinf/4-sinf 4-Sinf Musiqa/001_Vatanimizni madh etamiz.json:238>)

Band va naqarotli band shakllarida shå'riy va musiqiy tuzilmasining o'zaro munosabati qanday?

A) Shå'riy misralar to'rt, kuy ham to'rt; naqarot o'zgarmasdan bandlar orasida takrorlanadi | B) Har safar boshqacha | C) Bog'lanmagani | D) Musiqiy tuzilma davomiyligi

Belgilangan javob: A

“shå’riy”/“Shå’riy” ko‘rinishidagi buzilgan yozuv mavjud.

**Tavsiya:** “she’riy”/“She’riy” ko‘rinishiga tuzatish.

## Jamlanma va qamrov muammolari

- 3-sinf/3-sinf 3-Sinf Ona tili: Alohida mavzu JSON testlari yo‘q
- 3-sinf/3-sinf 3-Sinf Tasviriy san’at: 9 ta alohida fayl tarkibi jamlanmada yo‘q; 0 ta jamlanma yozuvi alohida fayllarda yo‘q
- 3-sinf/3-sinf 3-Sinf Texnologiya: 31 ta alohida fayl tarkibi jamlanmada yo‘q; 0 ta jamlanma yozuvi alohida fayllarda yo‘q
- 4-sinf/4-sinf 4-Sinf Matematika: 26 ta alohida fayl tarkibi jamlanmada yo‘q; 0 ta jamlanma yozuvi alohida fayllarda yo‘q
- 4-sinf/4-sinf 4-Sinf Musiqa: 18 ta alohida fayl tarkibi jamlanmada yo‘q; 0 ta jamlanma yozuvi alohida fayllarda yo‘q
- 4-sinf/4-sinf 4-Sinf Odobnoma: 1 ta alohida fayl tarkibi jamlanmada yo‘q; 0 ta jamlanma yozuvi alohida fayllarda yo‘q

5 ta fan jamlanmasida jami 85 ta alohida mavzu mazmuni yo‘q. Jamlanmadan import qilinsa, ular nashrga tushmaydi. 204 ta fan/mavzu-raqami guruhida raqam takrorlangan; to‘plam versiyasi yoki noyob identifikator bilan farqlash lozim. Bu 204 ta noto‘g‘ri savol degani emas.

## Avtomatik tekshiruvning ijobiy natijalari

- JSON ochilish xatosi, bo‘sh savol, variantlar soni va javob indeksi xatosi topilmadi.
- Tekshirilgan alohida JSON va TXT nusxalari o‘zaro mos.
- Bir fan ichida aynan bir xil savol va variantlar to‘plami uchun turlicha javob kaliti topilmadi.
- 50 ta son qiymati tengligi signalining barchasi xato emas. Yuqoridagi 6-sinf 11- va 14-savollarida esa ikki to‘g‘ri javob borligi tasdiqlandi.
- 7-sinfdagi Å belgisi va 8-sinfdagi Adèle ismi o‘z-o‘zidan kodlash xatosi emas.

## Sinflar bo‘yicha qaror

- 3-sinf: matnsiz savollar, tahrir, yetishmayotgan Ona tili testlari va jamlanma muammolari hal qilinishi kerak.
- 4-sinf: noto‘g‘ri kalit, takror variant, buzilgan yozuv va jamlanmalar tuzatilishi kerak.
- 5-sinf: ko‘rilgan adabiyot savolida mazmunli tahrir zarur.
- 6-sinf: ikki to‘g‘ri javobli savollar va tushunarsiz adabiyot savoli qayta ishlanishi kerak.
- 7–9-sinflar: joriy avtomatik qoidalar aniq kalit xatosini ko‘rsatmadi; bu barcha javoblar mazmunan to‘g‘ri ekanini tasdiqlamaydi.

## Nashrga chiqarishdan oldin

1. Yuqoridagi tasdiqlangan muammolarni tuzatish va JSON/TXT/jamlanmani birga yangilash.
2. Parallel to‘plamlar qaysi darslik/nashrga tegishli ekanini belgilash, mavzu identifikatorlarini aniqlashtirish.
3. Matn/rasm/jadval talab qiluvchi testlarga tegishli manbani biriktirish.
4. Qolgan savollarni fanlar bo‘yicha mazmunan tekshirish; hozirgi avtomatik tekshiruvni to‘liq ekspertiza deb qabul qilmaslik.

Avvalgi TEKSHIRUV_HISOBOTI.md dagi 3 338 mavzu / 99 123 savol va “0 xato” natijasi hozirgi fayllarga to‘liq mos kelmaydi. Yangi tekshiruv shu sabab alohida saqlandi.
