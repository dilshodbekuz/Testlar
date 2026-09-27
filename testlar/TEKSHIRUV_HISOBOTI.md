# Testlar tekshiruvi — 3–9-sinflar

Tekshiruv sanasi: 2026-09-27.

Qayta nazorat: 2026-09-27 kuni barcha fayllar ikkinchi marta mustaqil yugurtirildi. Natija o‘zgarmadi; yangi tasdiqlangan savol xatosi topilmadi. Ikkinchi audit natijalari `audit/qayta_tekshiruv_2` papkasida saqlandi.

## Yakuniy holat

3–9-sinflardagi barcha 3,338 ta alohida mavzu JSON fayli va 99,123 ta savol tuzilma hamda avtomatik qoidalar bilan qayta tekshirildi. JSON ochilishi, savol matni, to‘rtta variant, javob indeksi, takror variant, arifmetik kalit, buzilgan kodlash, JSON–TXT va `_TOLIQ.json` mosligi nazorat qilindi.

Tuzatish jurnalida 1,346 ta noyob savol o‘zgarishi saqlandi. Dastlabki 861 ta ro‘yxatdan tashqari tizimli yozuv va mazmun xatolari ham aniqlangani uchun amaldagi tuzatish soni ko‘proq. Har bir o‘zgarishning oldingi va keyingi holati `audit/tuzatish_861/TUZATISHLAR.jsonl` faylida, zaxiralari esa shu papkadagi `zaxira_*` kataloglarida turibdi.

| Sinf | Mavzu fayli | Savol | Hisoblangan arifmetik savol | Tuzatilgan noyob savol | Tekshirilgan son signali | To‘g‘ri maxsus yozuv |
|---|---:|---:|---:|---:|---:|---:|
| 3-sinf | 530 | 15,778 | 578 | 811 | 13 | 0 |
| 4-sinf | 374 | 11,145 | 31 | 70 | 4 | 0 |
| 5-sinf | 390 | 11,610 | 44 | 243 | 4 | 0 |
| 6-sinf | 433 | 12,898 | 54 | 115 | 19 | 0 |
| 7-sinf | 501 | 14,610 | 8 | 66 | 4 | 3 |
| 8-sinf | 487 | 14,477 | 0 | 22 | 0 | 5 |
| 9-sinf | 623 | 18,605 | 7 | 19 | 2 | 0 |

## Qayta audit xulosasi

- Yaroqsiz JSON, bo‘sh savol, to‘rttadan boshqa variant yoki noto‘g‘ri javob indeksi: **0**.
- Bir savol ichidagi aynan takror variant: **0**.
- JSON–TXT yoki `_TOLIQ.json` bilan mazmun farqi: **0**.
- Noto‘g‘ri hisoblangan oddiy arifmetik kalit: **0**; 722 ta hisoblanadigan savol qayta hisoblandi.
- Aralash kirill-lotin harfi bilan buzilgan so‘z: **0**.
- Qolgan 46 ta `equivalent_numeric_options` signali qo‘lda ko‘rildi: savollar sonning yozilish shakli, xona qo‘shiluvchisi, tub ko‘paytuvchi, nisbat yoki daraja ko‘rinishini so‘ragani uchun ular bir ma’noli.
- Qolgan 8 ta `text_encoding` signali xato emas: 7-sinf kimyodagi `Å` o‘lchov belgisi (3 ta) va 8-sinf ingliz tilidagi `Adèle` ismi (5 ta).

7-sinf adabiyotdagi noto‘g‘ri `023_Furqat` nomi kitobdagi mazmunga muvofiq `023_Abdulla Qodiriy` deb tuzatildi. 6-sinf rus tili 008-mavzusidagi buzilgan izohlar va javoblar ravon, bir ma’noli shaklda qayta yozildi.

## Fayl darajasidagi eslatmalar

Audit 5 ta fan papkasida alohida mavzu testi yo‘qligini va asosan 3-sinfdagi ikki parallel to‘plam sabab 124 ta takror mavzu raqamini qayd etdi. Bular mavjud savollarning javob xatosi emas; manba to‘plamining tuzilish holati sifatida saqlandi.
