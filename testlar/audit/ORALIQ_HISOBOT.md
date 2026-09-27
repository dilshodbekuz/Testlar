# Testlar tekshiruvi — ORALIQ HISOBOT

**Holat: to‘liq mazmuniy tekshiruv yakunlanmagan. Bu yakuniy hisobot emas.**

Jami 83,312 ta savolning har biri avtomatik tuzilish tekshiruvidan o‘tdi. Shundan 2,708 ta savol matni, barcha variantlari va kaliti birma-bir o‘qib ko‘rildi. 80,604 ta savolning mazmuniy tekshiruvi hali bajarilmagan.

3-sinf matematika bo‘yicha 83 ta mavzu faylidagi 2 477 ta savol va Musiqa bo‘yicha 30 ta savol to‘liq o‘qildi. Odobnoma bo‘yicha 001–006 mavzulardagi 180 ta savol ham birma-bir o‘qildi. Boshqa fan/sinflarda avtomatik topilgan 21 ta savol alohida ko‘rildi. Manba talab qiladigan savollar javobi hali tasdiqlanmagan.

Asl JSON/TXT testlar o‘zgartirilmadi. Hisob alohida mavzu JSON fayllari bo‘yicha; _TOLIQ.json va TXT nusxalari qayta sanalmagan.

## Ko‘rilgan savollar natijasi

| Holat | Savollar soni |
|---|---:|
| Xato yoki bir ma’noli javob yo‘q | 87 |
| Tahrir / shartni aniqlashtirish | 227 |
| Manba yoki rasm kerak | 20 |
| Ko‘rildi, muammo qayd etilmadi | 2374 |

Muammo qayd etilmagani barcha tarixiy, biologik yoki o‘quv dasturiga oid faktlar tashqi manbalar bilan tasdiqlandi degani emas. Matematik savollarda hisob, mantiq, yetarli shart va variantlarning bir ma’noliligi ko‘rildi. Imlo bo‘yicha lug‘at bilan to‘liq solishtirish bajarilmadi.

## Muhim misollar

- 3-sinf, Matematika, 024-mavzu, 17 va 25-savollar: 10, 20, 10 sm tomonli uchburchak mavjud emas; 10+10=20.
- 3-sinf, Matematika, 073-mavzu, 15-savol: chorshanbadan 32 kun oldin shanba bo‘ladi. Kalitdagi yakshanba xato.
- 3-sinf, Matematika, 036-mavzu, 30-savol: “ulardan 5 marta kam” shartiga ko‘ra jami 84 ko‘chat; 77 kaliti boshqa shartga mos.
- 3-sinf, Matematika, 034-mavzu, 20-savol: 29 minut 66 sekund va 30 minut 6 sekund teng; ikki javobni to‘g‘ri olish mumkin.
- 5-sinf, Matematika (2-qism), 006-mavzu, 23-savol: 19/21−16/21+7/21=10/21. Kalit 11/21 noto‘g‘ri.
- 6-sinf, Matematika, 006-mavzu, 30-savol: 2+(−5)×2=−8. Kalit −6 noto‘g‘ri.
- Odobnoma, 002-mavzu, 13-savol: Humo qushiga xavfsizlik va tinchlik ma’nosi berilgan; to‘g‘ri javob baxt va erksevarlik. 005-mavzudagi 17 va 30-savollarda Arastuning so‘zlari uning o‘g‘liga noto‘g‘ri nisbat berilgan.
- Musiqa: 30 ta savolning barchasi musiqa mavzusiga mos emas. Ayrimlarida kalit, ma’no va imlo xatolari ham bor.
- Eyfel minorasi balandligi haqidagi 320 m qiymati davrsiz berilgan. Hozirgi antenna bilan balandlik 330 m; unga bog‘liq hisoblar yangilanishi kerak. [Eyfel minorasi rasmiy manbasi](https://www.toureiffel.paris/en/news/events/eiffel-tower-grows-330-meters-tall).

## Sinflar bo‘yicha qamrov

| Sinf | Mavzu fayllari | Savollar | Mazmunan ko‘rildi | Mazmunan ko‘rilmagan |
|---|---:|---:|---:|---:|
| 3-sinf | 464 | 13810 | 2688 | 11122 |
| 4-sinf | 314 | 9347 | 3 | 9344 |
| 5-sinf | 390 | 11610 | 5 | 11605 |
| 6-sinf | 396 | 11795 | 12 | 11783 |
| 7-sinf | 501 | 14610 | 0 | 14610 |
| 8-sinf | 339 | 10051 | 0 | 10051 |
| 9-sinf | 405 | 12089 | 0 | 12089 |

## Avtomatik tekshiruv chegarasi

- Barcha mavzu JSON fayllari ochildi. Savol va variantlarning bo‘shligi, 4 ta variant mavjudligi, javob indeksining 0–3 oralig‘ida bo‘lishi tekshirildi. Ushbu tuzilish buzilishlari aniqlanmadi.
- TXT nusxalar savol matni, variantlar va javob belgisi bo‘yicha JSON bilan solishtirildi. Mazmuniy nusxa farqi aniqlanmadi.
- Aynan takroriy variantli 14 ta savol topildi. Oldingi dastlabki hisobot katta-kichik harflarni tenglashtirgani uchun biologiyadagi AA/Aa/aa kabi variantlarni noto‘g‘ri belgilagan; o‘sha hisoblar ushbu hisobot bilan almashtirildi.
- 92 ta teng son qiymatli variant holati va 616 ta g‘ayrioddiy belgi signali bor. Bularning hammasi xato deb tasdiqlanmagan.
- Oddiy arifmetik shablonga mos 709 ta savol avtomatik hisoblandi; 2 ta noto‘g‘ri kalit va 6 ta bir nechta to‘g‘ri sonli variant topilib, qo‘lda ham tekshirildi.
- 17 ta fan papkasida alohida mavzu testlari yo‘q. 3-sinfning 4 fanida jamlanma va alohida fayllar tarkibi farq qiladi; 124 ta mavzu raqami bir nechta faylda ishlatilgan.

## Batafsil fayllar

- [Savol, variant, kalit va tuzatish izohlari](</Users/dilshodbek/Desktop/Testlar/testlar/audit/MAZMUNIY_TOPILMALAR.md>)
- [Fanlar bo‘yicha qamrov](</Users/dilshodbek/Desktop/Testlar/testlar/audit/TEKSHIRUV_QAMROVI.md>)
- [Avtomatik signallar](</Users/dilshodbek/Desktop/Testlar/testlar/audit/AVTOMATIK_TOPILMALAR.md>)
- [Fayl va jamlanma muammolari](</Users/dilshodbek/Desktop/Testlar/testlar/audit/FAYL_TOPILMALARI.md>)
- [Har bir savolning alohida holati — JSONL](</Users/dilshodbek/Desktop/Testlar/testlar/audit/savollar_holati.jsonl>)

## Qolgan ish

80,604 savolni ketma-ket mazmunan o‘qish, manba/rasm talab qiladigan savollarni asl darslik bilan tekshirish, qolgan 92 ta teng qiymat signali va matn buzilishlarini kontekstda saralash kerak. Shundan keyingina yakuniy umumiy xulosa berish mumkin.
