# Test tekshirish qo'llanmasi (agentlar uchun)

Maqsad: berilgan kitob(lar)dagi HAR BIR savolni o'qib, xatolarni TUZATISH.
Til: o'zbek (lotin). Darslik PDF'ini o'qima — faqat savollarning o'zini tekshir.

## Vositalar (papka: /Users/dilshodbek/Desktop/Testlar/testlar/audit/vosita)
Ko'rish (6 tadan mavzu, chiqish ~30KB bo'lsa faylga yoz va Read bilan o'qi):
    python3 show.py "<kitob papkasi nomi>" <dan> <gacha> > ish/<ID>/r.txt
    python3 show.py "<kitob>" "12:5,12:7"     # aniq savollar
Chiqish: `N. savol || A | *B | C | D`  — `*` = hozirgi kalit.

Tuzatish: ish/<ID>/fN.txt fayliga qatorlar yoz, keyin `python3 apply.py ish/<ID>/fN.txt`
Qator formati (| bilan 6 maydon):
    <kitob papkasi nomi>|<mavzu raqami>|<savol raqami>|<yangi kalit A-D yoki ->|<yangi savol matni yoki ->|<variantlar yoki ->
Variantlar: to'liq 4 tasi `v1;;v2;;v3;;v4` YOKI faqat o'zgarganlari `B=matn;;D=matn`.
Misollar:
    4-sinf 4-Sinf Matematika|21|7|C|-|-                       (faqat kalit)
    4-sinf 4-Sinf Matematika|21|7|-|-|D=1/9                   (bitta variant)
    4-sinf 4-Sinf Matematika|3|5|B|Yangi savol?|a;;b;;c;;d    (to'liq qayta yozish)
apply.py .json, .txt va _TOLIQ.json ni yangilaydi. 4 variant har xil bo'lishi shart (aks holda xato beradi — tuzatib qayta ishga tushir; xato qatorgacha hech narsa yozilmaydi).
Bash'da `$` va backtick belgilariga ehtiyot bo'l: fix faylini Write tool bilan yoz.

## MUHIM: takroriy mavzu raqamlari
Ba'zi kitoblarda (3-sinf O'qish, Tabiatshunoslik, Tarbiya, Tasviriy san'at) bitta raqamda ikkita
fayl bor. show.py ularni `## 008a ...` va `## 008b ...` deb ko'rsatadi. Fix qatorida mavzu
maydoniga aynan shu belgini yoz: `...|8a|5|...` yoki `...|8b|5|...`. Harfsiz yozsang apply.py
xato berib to'xtaydi. Ikkala faylni ham tekshirish kerak — ular alohida testlar.

## Nimani tuzatish kerak (muhimlik tartibida)
1. Kalit noto'g'ri (hisob, fakt, grammatika) — to'g'ri variantga o'zgartir. Hisoblarni qayta hisobla.
2. Ikki yoki undan ko'p variant to'g'ri / teng qiymatli (masalan 1/2 va 2/4, "Hammasi" + to'g'ri variant) — chalg'ituvchini almashtir.
3. To'g'ri javob variantlarda yo'q yoki shart yetishmaydi — savolni/variantlarni tuzat.
4. Ma'nosiz, buzilgan (kirill-lotin aralash, tushunarsiz so'zlar) savol yoki KALIT matni — tushunarli qilib qayta yoz.
5. Fanga/mavzuga aloqasiz yoki matnsiz tekshirib bo'lmaydigan ("matnda nechta..." kabi, javobi taxmin) savol — o'rniga shu mavzu bo'yicha aniq, tekshiriladigan savol yoz (qiyinlik saqlansin).
Chalg'ituvchilardagi mayda imlo xatolariga vaqt sarflama (faqat juda buzuq bo'lsa).

QAT'IY BO'L: 3–6-sinf testlarini zaif model yozgan. Tajribada har 30 savollik mavzuda odatda 3–10 ta
tuzatiladigan savol chiqadi. "Xato topilmadi" deyishdan oldin qayta tekshir. Tipik xatolar:
- kalit matni buzuq/ma'nosiz ("Ushbu ikki illatning insonda ko'proq buzuv olib keladi"), yoki
  savolda so'ralganining teskarisi (masalan "xalaqit bermaslik kerak" savoliga kalit "xalaqit qilasiz");
- chalg'ituvchi ham to'g'ri (masalan "Kitobni qayerda saqlash kerak? Polkada | *Javonda");
- "Hammasi to'g'ri" varianti, lekin boshqa variantlardan biri noto'g'ri;
- tarjima/lug'at xatosi (masalan "mo'l" = ko'p, kalit "qiyin" bo'lgan);
- sanoq/hisob xatosi (shanba 6-kun, 7-emas);
- "matnda nechta ..." kabi darsliksiz tekshirib bo'lmaydigan savol — lug'at yoki qoida savoliga almashtir.
Qayta yozilgan savollarda to'g'ri javob o'rnini A..D orasida aralashtir (doim A bo'lmasin).
Ishonching komil bo'lmasa (darslik matniga bog'liq hikoya tafsiloti) — tegma.

## Tartib
- Faqat SENGA berilgan kitoblarga teg (boshqa agentlar parallel ishlayapti).
- Har kitobni boshidan oxirigacha 5-6 mavzudan o'qi, tuzat, keyingisiga o't.
- HAR BIR 5-6 mavzulik bo'lak tugashi bilan `ish/<ID>/tayyor.txt` ga "kitob|mavzu N-M tayyor" qatorini qo'sh (limit tugab to'satdan to'xtashing mumkin — progress yo'qolmasin).
- Har bir tugagan kitobni `ish/<ID>/tayyor.txt` ga bitta qator qilib yoz (qayta ishga tushsa davom etish uchun). Boshlashda shu faylni tekshir va tayyorlarini o'tkazib yubor.
- Oxirida qisqa hisobot qaytar: kitob, nechta savol tuzatildi, eng muhim 3-5 misol (fayl:savol — nima edi → nima bo'ldi).
