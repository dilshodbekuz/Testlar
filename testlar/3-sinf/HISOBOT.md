# 3-sinf testlari tekshiruv hisoboti

Tekshiruv sanasi: 2026-09-27.

## Xulosa

9 ta test mavjud fan papkasidagi 530 ta alohida mavzu fayli va 15,778 ta savol qayta tekshirildi. 572 ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.

Oldingi tuzatish jurnalida 2,435 ta alohida savol bor. Ulardan 2,418 tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning 2,435/2,435 tasi amaldagi faylga mos.

## Fanlar bo‘yicha qamrov

| Fan | Mavzu fayli | Savol | Avtomatik signal |
|---|---:|---:|---:|
| 3-Sinf Ingliz tili | 67 | 1998 | 0 |
| 3-Sinf Matematika | 83 | 2477 | 13 |
| 3-Sinf Odobnoma | 24 | 716 | 0 |
| 3-Sinf O‘qish | 164 | 4865 | 559 |
| 3-Sinf Rus tili | 24 | 717 | 0 |
| 3-Sinf Tabiatshunoslik | 72 | 2148 | 0 |
| 3-Sinf Tarbiya | 21 | 621 | 0 |
| 3-Sinf Tasviriy san’at | 45 | 1340 | 0 |
| 3-Sinf Texnologiya | 30 | 896 | 0 |

## Savol signallari

- G‘ayrioddiy yoki buzilgan belgi: 559 ta.
- Teng son qiymatli variantlar: 13 ta.
- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: 578 ta.
- Noto‘g‘ri arifmetik kalit signali: 0 ta.

Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.

## Kirill-lotin aralash yozuv

Rus tili fanidan tashqari 74 ta savolda bitta so‘z ichida kirill va lotin harflari aralashgani tasdiqlandi. Ular [TASDIQLANGAN_ARALASH_ALIFBO.csv](TASDIQLANGAN_ARALASH_ALIFBO.csv) fayliga chiqarildi.

## Fayl va jamlanma holati

- Testi yo‘q fan papkasi: 2 ta.
- Jamlanma bilan alohida fayllar farqi: 4 ta fan papkasida.
- Takror ishlatilgan mavzu raqami: 124 ta holat.

Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.

## Takroriy savollarni qo‘lda solishtirish

Bir xil matnli savollarning 59 ta ehtimoliy ziddiyat guruhi qo‘lda ko‘rildi. 7 guruhda xato yoki noaniqlik tasdiqlandi, 52 guruhdagi javoblar mazmunan mos yoki alohida dars/matn kontekstiga bog‘liq. Tafsilotlar [TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv](TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv) va [MOS_TAKRORIY_JAVOBLAR.csv](MOS_TAKRORIY_JAVOBLAR.csv) fayllarida.

## Tekshiruv chegarasi

Matn, rasm, jadval, she’r, hikoya yoki asarga bog‘langan 1 052 ta savol [MANBA_TALAB_QILADIGAN_SAVOLLAR.csv](MANBA_TALAB_QILADIGAN_SAVOLLAR.csv) fayliga chiqarildi. Ularning javobi asl kontekstsiz yakuniy tasdiqlanmaydi.

Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.

Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.
