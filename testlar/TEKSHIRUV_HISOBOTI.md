# Testlar tekshiruvi — 3–9-sinflar

Tekshiruv sanasi: 2026-09-27.

## Umumiy natija

Barcha mavjud alohida mavzu JSON fayllari texnik va avtomatik qoidalar bilan qayta tekshirildi. Hisobotlar har bir sinf papkasiga yozildi. Test fayllarining o‘zi o‘zgartirilmadi.

| Sinf | Mavzu fayli | Savol | Signal tushgan savol | Hisoblangan arifmetik savol | Oldingi qo‘llangan tuzatish |
|---|---:|---:|---:|---:|---:|
| 3-sinf | 530 | 15,778 | 572 | 578 | 2,435 |
| 4-sinf | 374 | 11,145 | 36 | 31 | 57 |
| 5-sinf | 390 | 11,610 | 5 | 44 | 54 |
| 6-sinf | 433 | 12,898 | 39 | 54 | 62 |
| 7-sinf | 501 | 14,610 | 5 | 8 | 2 |
| 8-sinf | 487 | 14,477 | 5 | 0 | 1 |
| 9-sinf | 623 | 18,605 | 2 | 7 | 2 |

## Jami

- Mavzu fayllari: 3,338 ta.
- Savollar: 99,123 ta.
- Signal tushgan savollar: 664 ta.
- Oddiy arifmetik shaklda qayta hisoblangan savollar: 722 ta.
- Tuzilish xatosi, bo‘sh savol, noto‘g‘ri variant soni yoki yaroqsiz javob indeksi topilmadi.

Har bir sinfning batafsil natijasi o‘sha sinf papkasidagi `HISOBOT.md`, `MUAMMOLI_SAVOLLAR.csv` va `FAYL_MUAMMOLARI.csv` fayllarida.

## Takroriy savollarni solishtirish

Bir xil savol matniga turli javoblar belgilangan 209 ta guruh qo‘lda solishtirildi. 20 guruhda haqiqiy ziddiyat, matn xatosi yoki kontekstsiz noaniqlik tasdiqlandi; 189 guruhdagi javoblar mazmunan teng yoki alohida dars, matn va laboratoriya kontekstiga bog‘liq.

| Sinf | Ko‘rilgan guruh | Tasdiqlangan muammo | Mos/kontekstga bog‘liq |
|---|---:|---:|---:|
| 3-sinf | 59 | 7 | 52 |
| 4-sinf | 13 | 0 | 13 |
| 5-sinf | 21 | 2 | 19 |
| 6-sinf | 15 | 5 | 10 |
| 7-sinf | 45 | 1 | 44 |
| 8-sinf | 31 | 0 | 31 |
| 9-sinf | 25 | 5 | 20 |

Har bir sinf papkasida `TAKRORIY_SAVOLLAR.csv`, `ZIDDIYATLI_TAKRORLAR.csv`, `TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv` va `MOS_TAKRORIY_JAVOBLAR.csv` saqlandi.

## Signallarni qo‘lda saralash natijasi

- **3-sinf:** O‘qish fanidagi buzilgan harflar haqiqiy tahrir muammosi. Matematika signallarining ko‘pi savol aynan xona qo‘shiluvchilari yoki yozilish shaklini so‘ragani uchun avtomatik xato emas. Oldingi batafsil auditda 186 ta tahrir/manba qaydi bor.
- **4-sinf:** Ingliz tilidagi `Syrdårya`, Musiqadagi `shå'riy`, Ona tilidagi `Ò` bilan buzilgan so‘zlar va Texnologiyadagi `Machtà` haqiqiy matn muammolari. Matematika 007-mavzu 5-savolda to‘rtta variantning ham qiymati 1 800 bo‘lib, savol bir ma’noli emas.
- **5-sinf:** to‘rtta matematik signal savolning talabiga ko‘ra bir ma’noli; xato deb tasdiqlanmadi. Tasviriy san’atdagi `Milân` yozuvi `Milan` shaklida tahrir talab qiladi.
- **6-sinf:** Geografiya, Ona tili, Rus tili va Vatan tuyg‘usidagi 20 ta buzilgan belgi haqiqiy matn muammosi. Matematika signallarining aksariyatida aynan tub ko‘paytuvchilarga yoyish yoki eng sodda nisbat so‘ralgan. `011_Nisbat tushunchasi. Proporsiyalar.json`, 19-savolda esa 2:3, 4:6 va 6:9 bir xil nisbat bo‘lib, bir nechta to‘g‘ri variant mavjud.
- **7-sinf:** `Å` belgisi va Al-Xorazmiy yillari bo‘yicha avtomatik signallar xato emas. Biroq `023_Furqat.json` faylidagi 30 savolning barchasi Furqat o‘rniga Abdulla Qodiriy haqida ekani hamda bitta takroriy quvvat savoli noaniq ekani qo‘lda tasdiqlandi.
- **8-sinf:** `Adèle` fransuzcha ismning to‘g‘ri yozilishi. Avtomatik va takroriy savol signallaridan bevosita javob xatosi tasdiqlanmadi; 22 ta aralash alifboli buzilish alohida ro‘yxatga olindi.
- **9-sinf:** geometriya nisbatlari to‘g‘ri. Qo‘lda takror solishtirishda bitta noaniq algebra savoli va biologiyadagi to‘rtta qarama-qarshi javob kaliti tasdiqlandi.

## Manbaga bog‘liq savollar

Matn, rasm, jadval, she’r, hikoya yoki asarga tayangan 6 942 ta savol sinflar kesimida `MANBA_TALAB_QILADIGAN_SAVOLLAR.csv` fayllariga ajratildi. Asl matn yoki rasm test faylida mavjud bo‘lmagan hollarda javobni mustaqil ravishda yakuniy tasdiqlash imkoni yo‘q; shu sabab bu savollar hisobotda alohida ochiq tekshiruv toifasi sifatida saqlandi.

Test JSON/TXT fayllari o‘zgartirilmadi. Faqat tekshiruv hisobotlari va CSV ro‘yxatlari yozildi.
