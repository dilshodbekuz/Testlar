# 7-sinf testlari tekshiruv hisoboti

Tekshiruv sanasi: 2026-09-27.

## Xulosa

13 ta test mavjud fan papkasidagi 501 ta alohida mavzu fayli va 14,610 ta savol qayta tekshirildi. 5 ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.

Oldingi tuzatish jurnalida 2 ta alohida savol bor. Ulardan 2 tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning 2/2 tasi amaldagi faylga mos.

## Fanlar bo‘yicha qamrov

| Fan | Mavzu fayli | Savol | Avtomatik signal |
|---|---:|---:|---:|
| 7-Sinf Adabiyot | 30 | 870 | 0 |
| 7-Sinf Algebra | 26 | 772 | 4 |
| 7-Sinf Fizika | 27 | 798 | 0 |
| 7-Sinf Geografiya | 42 | 1223 | 0 |
| 7-Sinf Geometriya | 13 | 378 | 0 |
| 7-Sinf Informatika | 16 | 473 | 0 |
| 7-Sinf Ingliz tili | 59 | 1707 | 0 |
| 7-Sinf Jahon tarixi | 34 | 980 | 0 |
| 7-Sinf Kimyo | 37 | 1095 | 3 |
| 7-Sinf Ona tili | 61 | 1783 | 0 |
| 7-Sinf O‘zbekiston tarixi | 26 | 754 | 0 |
| 7-Sinf Texnologiya | 56 | 1629 | 0 |
| 7-Sinf Zoologiya | 74 | 2148 | 0 |

## Qo‘lda saralash

7 ta signalning barchasi qo‘lda ko‘rildi. `Å` angstromning to‘g‘ri belgisi; Al-Xorazmiy yillari bo‘yicha signallar yil oralig‘i tufayli chiqqan. Bu signallardan tasdiqlangan xato qolmadi.

Adabiyotdagi `023_Furqat.json` fayli alohida tekshirildi. Fayl va mavzu nomi Furqat bo‘lsa-da, undagi 30 savolning barchasi Abdulla Qodiriy hayoti va asarlari haqida. Har bir savol [QOLDA_TASDIQLANGAN_MUAMMOLAR.csv](QOLDA_TASDIQLANGAN_MUAMMOLAR.csv) fayliga yozildi.

[Xato emas deb saralangan signallar](XATO_EMAS_SIGNALLAR.csv)

## Savol signallari

- G‘ayrioddiy yoki buzilgan belgi: 3 ta.
- Teng son qiymatli variantlar: 4 ta.
- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: 8 ta.
- Noto‘g‘ri arifmetik kalit signali: 0 ta.

Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.

## Kirill-lotin aralash yozuv

Rus tili fanidan tashqari 66 ta savolda kirill va lotin harflari aralashgan. 65 tasi bitta so‘z ichidagi aniq buzilish sifatida [TASDIQLANGAN_ARALASH_ALIFBO.csv](TASDIQLANGAN_ARALASH_ALIFBO.csv) fayliga yozildi; 1 ta alohida kirillcha so‘z [ALOHIDA_KIRILL_SOZLAR.csv](ALOHIDA_KIRILL_SOZLAR.csv) faylida tekshiruvga qoldirildi.

Qolgan bitta `Донолик` tokeni ham lotin yozuvidagi savolda aloqasiz kirillcha so‘z sifatida tasdiqlandi: [TASDIQLANGAN_ALOHIDA_KIRILL.csv](TASDIQLANGAN_ALOHIDA_KIRILL.csv).

## Fayl va jamlanma holati

- Testi yo‘q fan papkasi: 0 ta.
- Jamlanma bilan alohida fayllar farqi: 0 ta fan papkasida.
- Takror ishlatilgan mavzu raqami: 0 ta holat.

Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.

## Takroriy savollarni qo‘lda solishtirish

Bir xil matnli savollarning 45 ta ehtimoliy ziddiyat guruhi qo‘lda ko‘rildi. 1 guruhda kontekstsiz noaniq savol tasdiqlandi, 44 guruh mazmunan mos yoki alohida matn/mavzu kontekstiga bog‘liq. Tafsilotlar [TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv](TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv) va [MOS_TAKRORIY_JAVOBLAR.csv](MOS_TAKRORIY_JAVOBLAR.csv) fayllarida.

## Tekshiruv chegarasi

Matn, rasm, jadval, she’r, hikoya yoki asarga bog‘langan 851 ta savol [MANBA_TALAB_QILADIGAN_SAVOLLAR.csv](MANBA_TALAB_QILADIGAN_SAVOLLAR.csv) fayliga chiqarildi. Ularning javobi asl kontekstsiz yakuniy tasdiqlanmaydi.

Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.

Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.
