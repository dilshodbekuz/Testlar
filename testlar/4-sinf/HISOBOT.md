# 4-sinf testlari tekshiruv hisoboti

Tekshiruv sanasi: 2026-09-27.

## Xulosa

11 ta test mavjud fan papkasidagi 374 ta alohida mavzu fayli va 11,145 ta savol qayta tekshirildi. 36 ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.

Oldingi tuzatish jurnalida 57 ta alohida savol bor. Ulardan 57 tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning 57/57 tasi amaldagi faylga mos.

## Fanlar bo‘yicha qamrov

| Fan | Mavzu fayli | Savol | Avtomatik signal |
|---|---:|---:|---:|
| 4-Sinf Ingliz tili | 60 | 1798 | 3 |
| 4-Sinf Matematika | 28 | 840 | 5 |
| 4-Sinf Musiqa | 27 | 800 | 5 |
| 4-Sinf Odobnoma | 36 | 1070 | 0 |
| 4-Sinf Ona tili | 17 | 507 | 21 |
| 4-Sinf O‘qish | 36 | 1069 | 0 |
| 4-Sinf O‘qish (metodika) | 23 | 685 | 0 |
| 4-Sinf Rus tili | 42 | 1253 | 0 |
| 4-Sinf Tabiatshunoslik | 33 | 982 | 0 |
| 4-Sinf Tasviriy san’at | 23 | 684 | 0 |
| 4-Sinf Texnologiya | 49 | 1457 | 2 |

## Qo‘lda tasdiqlangan natija

- 36 ta avtomatik signalning barchasi qo‘lda ko‘rildi.
- 31 ta buzilgan/g‘ayrioddiy belgi haqiqiy matn xatosi deb tasdiqlandi.
- Matematika 007-mavzu 5-savol bir nechta to‘g‘ri javobli savol deb tasdiqlandi: to‘rtta variantning ham qiymati 1 800.
- Qolgan 4 ta matematik signal xato emas: faqat kalit savolda talab qilingan to‘liq xona qo‘shiluvchilari yozuviga mos.

Tasdiqlangan 32 ta muammoning to‘liq ro‘yxati [TASDIQLANGAN_MUAMMOLAR.csv](TASDIQLANGAN_MUAMMOLAR.csv) faylida.

## Savol signallari

- G‘ayrioddiy yoki buzilgan belgi: 31 ta.
- Teng son qiymatli variantlar: 5 ta.
- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: 31 ta.
- Noto‘g‘ri arifmetik kalit signali: 0 ta.

Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.

## Kirill-lotin aralash yozuv

Rus tili fanidan tashqari 39 ta savolda kirill va lotin harflari aralashgan. Shundan 38 tasi bitta so‘z ichidagi aniq buzilish sifatida [TASDIQLANGAN_ARALASH_ALIFBO.csv](TASDIQLANGAN_ARALASH_ALIFBO.csv) fayliga, 1 tasi alohida kirillcha so‘z sifatida [ALOHIDA_KIRILL_SOZLAR.csv](ALOHIDA_KIRILL_SOZLAR.csv) fayliga yozildi.

## Fayl va jamlanma holati

- Testi yo‘q fan papkasi: 0 ta.
- Jamlanma bilan alohida fayllar farqi: 0 ta fan papkasida.
- Takror ishlatilgan mavzu raqami: 0 ta holat.

Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.

## Takroriy savollarni qo‘lda solishtirish

Bir xil matnli savollarning 13 ta ehtimoliy ziddiyat guruhi qo‘lda ko‘rildi. Javoblar mazmunan mos yoki alohida asar/hudud kontekstiga bog‘liq; bevosita ziddiyat tasdiqlanmadi. Natija [MOS_TAKRORIY_JAVOBLAR.csv](MOS_TAKRORIY_JAVOBLAR.csv) faylida.

## Tekshiruv chegarasi

Matn, rasm, jadval, she’r, hikoya yoki asarga bog‘langan 662 ta savol [MANBA_TALAB_QILADIGAN_SAVOLLAR.csv](MANBA_TALAB_QILADIGAN_SAVOLLAR.csv) fayliga chiqarildi. Ularning javobi asl kontekstsiz yakuniy tasdiqlanmaydi.

Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.

Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.
