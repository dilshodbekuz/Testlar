# 5-sinf testlari tekshiruv hisoboti

Tekshiruv sanasi: 2026-09-27.

## Xulosa

14 ta test mavjud fan papkasidagi 390 ta alohida mavzu fayli va 11,610 ta savol qayta tekshirildi. 5 ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.

Oldingi tuzatish jurnalida 54 ta alohida savol bor. Ulardan 54 tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning 54/54 tasi amaldagi faylga mos.

## Fanlar bo‘yicha qamrov

| Fan | Mavzu fayli | Savol | Avtomatik signal |
|---|---:|---:|---:|
| 5-Sinf Adabiyot | 22 | 651 | 0 |
| 5-Sinf Biologiya | 13 | 385 | 0 |
| 5-Sinf Geografiya | 23 | 683 | 0 |
| 5-Sinf Informatika | 32 | 950 | 0 |
| 5-Sinf Ingliz tili | 13 | 386 | 0 |
| 5-Sinf Matematika (1-qism) | 36 | 1079 | 4 |
| 5-Sinf Matematika (2-qism) | 20 | 599 | 0 |
| 5-Sinf Musiqa | 29 | 860 | 0 |
| 5-Sinf Ona tili | 52 | 1545 | 0 |
| 5-Sinf Rus tili | 30 | 891 | 0 |
| 5-Sinf Tarixdan hikoyalar | 34 | 1015 | 0 |
| 5-Sinf Tasviriy san’at | 12 | 358 | 1 |
| 5-Sinf Texnologiya | 64 | 1910 | 0 |
| 5-Sinf Vatan tuyg‘usi | 10 | 298 | 0 |

## Qo‘lda saralash

5 ta signalning barchasi qo‘lda ko‘rildi. Tasviriy san’atdagi `Milân` yozuvi matn xatosi deb tasdiqlandi. To‘rtta matematika signali savol talabi sabab bir ma’noli bo‘lib, xato emas.

- [Tasdiqlangan muammo](TASDIQLANGAN_MUAMMOLAR.csv)
- [Xato emas deb saralangan signallar](XATO_EMAS_SIGNALLAR.csv)

## Savol signallari

- G‘ayrioddiy yoki buzilgan belgi: 1 ta.
- Teng son qiymatli variantlar: 4 ta.
- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: 44 ta.
- Noto‘g‘ri arifmetik kalit signali: 0 ta.

Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.

## Kirill-lotin aralash yozuv

Rus tili fanidan tashqari 309 ta savolda kirill va lotin harflari aralashgan. Shundan 238 tasi bitta so‘z ichidagi aniq buzilish sifatida [TASDIQLANGAN_ARALASH_ALIFBO.csv](TASDIQLANGAN_ARALASH_ALIFBO.csv) fayliga yozildi; 71 ta alohida kirillcha so‘z/iqtibos [ALOHIDA_KIRILL_SOZLAR.csv](ALOHIDA_KIRILL_SOZLAR.csv) faylida tekshiruvga qoldirildi.

Alohida kirillcha tokenlarning 3 tasi Ingliz tili, Musiqa va Tarixdan hikoyalar fanlarida aloqasiz kirillcha so‘z sifatida tasdiqlandi: [TASDIQLANGAN_ALOHIDA_KIRILL.csv](TASDIQLANGAN_ALOHIDA_KIRILL.csv). Qolganlari asosan Informatika dasturlarining ruscha menyu nomlari bo‘lib, [TEKSHIRILADIGAN_KIRILL_IQTIBOSLAR.csv](TEKSHIRILADIGAN_KIRILL_IQTIBOSLAR.csv) faylida saqlandi.

## Fayl va jamlanma holati

- Testi yo‘q fan papkasi: 0 ta.
- Jamlanma bilan alohida fayllar farqi: 0 ta fan papkasida.
- Takror ishlatilgan mavzu raqami: 0 ta holat.

Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.

## Takroriy savollarni qo‘lda solishtirish

Bir xil matnli savollarning 21 ta ehtimoliy ziddiyat guruhi qo‘lda ko‘rildi. 2 guruhda muammo tasdiqlandi, 19 guruhdagi javoblar mazmunan mos. Tafsilotlar [TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv](TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv) va [MOS_TAKRORIY_JAVOBLAR.csv](MOS_TAKRORIY_JAVOBLAR.csv) fayllarida.

## Tekshiruv chegarasi

Matn, rasm, jadval, she’r, hikoya yoki asarga bog‘langan 511 ta savol [MANBA_TALAB_QILADIGAN_SAVOLLAR.csv](MANBA_TALAB_QILADIGAN_SAVOLLAR.csv) fayliga chiqarildi. Ularning javobi asl kontekstsiz yakuniy tasdiqlanmaydi.

Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.

Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.
