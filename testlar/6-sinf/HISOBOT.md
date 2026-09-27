# 6-sinf testlari tekshiruv hisoboti

Tekshiruv sanasi: 2026-09-27.

## Xulosa

14 ta test mavjud fan papkasidagi 433 ta alohida mavzu fayli va 12,898 ta savol qayta tekshirildi. 39 ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.

Oldingi tuzatish jurnalida 62 ta alohida savol bor. Ulardan 62 tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning 62/62 tasi amaldagi faylga mos.

## Fanlar bo‘yicha qamrov

| Fan | Mavzu fayli | Savol | Avtomatik signal |
|---|---:|---:|---:|
| 6-Sinf Adabiyot (1-qism) | 10 | 294 | 0 |
| 6-Sinf Adabiyot (2-qism) | 11 | 327 | 0 |
| 6-Sinf Botanika | 37 | 1103 | 0 |
| 6-Sinf Fizika | 24 | 718 | 0 |
| 6-Sinf Geografiya | 61 | 1815 | 1 |
| 6-Sinf Informatika | 24 | 712 | 0 |
| 6-Sinf Informatika (1) | 12 | 358 | 0 |
| 6-Sinf Informatika (2) | 14 | 419 | 0 |
| 6-Sinf Ingliz tili | 77 | 2299 | 0 |
| 6-Sinf Matematika | 18 | 539 | 19 |
| 6-Sinf Ona tili | 46 | 1370 | 15 |
| 6-Sinf Rus tili | 37 | 1098 | 3 |
| 6-Sinf Tarix | 44 | 1309 | 0 |
| 6-Sinf Vatan tuyg‘usi | 18 | 537 | 1 |

## Qo‘lda saralash

39 ta signalning barchasi qo‘lda ko‘rildi. 20 ta buzilgan matn va `011_Nisbat tushunchasi. Proporsiyalar.json` faylidagi 19-savol tasdiqlangan muammo. Bu savolda 2:3, 4:6 va 6:9 variantlari teng. Qolgan 18 ta matematik signal xato emas.

Oldingi ish jurnalidagi topilmalar amaldagi fayllarda qayta tekshirildi. Geografiyada 2 ta noto‘g‘ri kalit, 1 ta to‘g‘ri varianti yo‘q savol va `gipoteza` so‘zi buzilgan 10 ta savol tasdiqlandi. Rus tilida 1 ta o‘qib bo‘lmaydigan savol va 008-mavzudagi kirillcha o‘zbek yozuvida berilgan 30 ta savol qayd etildi. Jami 44 ta qo‘lda tasdiqlangan qayd [QOLDA_TASDIQLANGAN_MUAMMOLAR.csv](QOLDA_TASDIQLANGAN_MUAMMOLAR.csv) faylida.

Bir xil matnli, lekin turli javob berilgan 15 ta takror guruhi ham ko‘rildi. 10 guruhdagi javoblar mazmunan mos. 5 guruhda haqiqiy muammo tasdiqlandi: ikki noaniq savol, bitta noto‘g‘ri tenglama kaliti, proporsiya ta’rifi va miqdor sonlar tasnifi. Batafsil: [TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv](TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv).

- [Tasdiqlangan 21 ta muammo](TASDIQLANGAN_MUAMMOLAR.csv)
- [Xato emas deb saralangan 18 ta signal](XATO_EMAS_SIGNALLAR.csv)

## Savol signallari

- G‘ayrioddiy yoki buzilgan belgi: 20 ta.
- Teng son qiymatli variantlar: 19 ta.
- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: 54 ta.
- Noto‘g‘ri arifmetik kalit signali: 0 ta.

Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.

## Kirill-lotin aralash yozuv

Rus tili fanidan tashqari 116 ta savolda kirill va lotin harflari aralashgan. 57 tasi (`o‘zgarди`, `tomonга`, `Kiwilар` kabi) bitta so‘z ichidagi aniq buzilish bo‘lib, [TASDIQLANGAN_ARALASH_ALIFBO.csv](TASDIQLANGAN_ARALASH_ALIFBO.csv) fayliga yozildi. 59 ta alohida kirillcha so‘z/iqtibos [ALOHIDA_KIRILL_SOZLAR.csv](ALOHIDA_KIRILL_SOZLAR.csv) faylida tekshiruvga qoldirildi.

Alohida tokenlardan yana 4 tasi Adabiyot, Fizika va Geografiya fanlarida haqiqiy matn buzilishi deb tasdiqlandi: [TASDIQLANGAN_ALOHIDA_KIRILL.csv](TASDIQLANGAN_ALOHIDA_KIRILL.csv). Qolgan 55 ta holat asosan Informatika dasturlarining ruscha interfeys nomlari bo‘lib, [TEKSHIRILADIGAN_KIRILL_IQTIBOSLAR.csv](TEKSHIRILADIGAN_KIRILL_IQTIBOSLAR.csv) faylida saqlandi.

## Fayl va jamlanma holati

- Testi yo‘q fan papkasi: 2 ta.
- Jamlanma bilan alohida fayllar farqi: 0 ta fan papkasida.
- Takror ishlatilgan mavzu raqami: 0 ta holat.

Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.

## Tekshiruv chegarasi

Matn, rasm, jadval, she’r, hikoya yoki asarga bog‘langan 826 ta savol [MANBA_TALAB_QILADIGAN_SAVOLLAR.csv](MANBA_TALAB_QILADIGAN_SAVOLLAR.csv) fayliga chiqarildi. Ularning javobi asl kontekstsiz yakuniy tasdiqlanmaydi.

Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.

Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.
