# Test Generator loyihasi

Maktab darsliklari (PDF) asosida har bir mavzu bo'yicha **30 ta test** yaratiladi:
**10 ta oson + 10 ta o'rtacha + 10 ta qiyin**. Til: o'zbek (lotin).

## Tuzilma
```
kitoblar/3-sinf/ ... kitoblar/11-sinf/   <- foydalanuvchi PDF kitoblarni shu yerga qo'yadi
testlar/<sinf>/<kitob>/                  <- natija (dastur yaratadi)
    _mavzular.json      mavzular ro'yxati va sahifa oralig'i
    001_<mavzu>.json    30 ta savol (saytga import uchun)
    001_<mavzu>.txt     o'qish uchun; to'g'ri javob oldida "+"
    _TOLIQ.json         kitobdagi hamma mavzular birlashgan
test_generator.py        asosiy dastur (sozlamalar fayl boshida)
```

## Buyruqlar
- Hammasi: `python test_generator.py`
- Bitta sinf yoki fan: `python test_generator.py 7-sinf` / `python test_generator.py Fizika`
- Progress: `python test_generator.py --holat`
- Limit tugasa dastur 1 daqiqa kutib o'zi qayta uradi; kutmaslik uchun `--bir-marta`
- Kutubxona (bir marta): `python -m pip install -r requirements.txt`

## Siz (Claude) uchun QAT'IY QOIDALAR
1. **Limitni teja.** Foydalanuvchining haftalik limiti tez tugaydi. Javoblar qisqa bo'lsin.
2. **PDF'larni o'zing o'qima va testlarni o'zing yozma.** Hamma ishni `test_generator.py` qiladi —
   u har bir mavzu uchun alohida qisqa `claude -p` so'rov yuboradi (kontekst to'planmaydi).
3. Dasturni **orqa fonda** ishga tushir (`run_in_background: true`) — u soatlab ishlaydi,
   oddiy Bash chaqiruvi vaqt chegarasiga uriladi. Keyin progressni `--holat` bilan ko'r.
4. Natija fayllarini butunlay o'qima. Tekshirish kerak bo'lsa bitta `.txt` fayldan 2-3 savolni ko'r.
5. "Limit tugadi" chiqsa — dastur o'zi 1 daqiqa kutib davom ettiradi (KUTISH_DAQIQA).
   Tayyor mavzular o'tkazib yuboriladi, ish qolgan joydan davom etadi.
6. Mavzular noto'g'ri ajratilgan bo'lsa: o'sha kitobning `_mavzular.json` faylini tuzat
   (yoki o'chir — qayta aniqlanadi), noto'g'ri mavzu `.json/.txt` larini o'chirib qayta ishga tushir.
7. Skaner (matnsiz) PDF'lar o'tkazib yuboriladi — foydalanuvchiga ro'yxatini ayt, o'zing OCR qilma
   (foydalanuvchi so'ramasa).
8. **Skaner PDF'ni matnga o'tkazish:** `ocr/README.md` ga qara. macOS'ning o'z OCR'i
   ishlatiladi (limit yemaydi, ~160 sahifa/daqiqa). Formulali fanlarga (Algebra,
   Fizika, Chizmachilik) YARAMAYDI — formulalar buziladi.

## Format (o'zgartirma)
```json
{"sinf": "7-sinf", "kitob": "Fizika", "mavzu": "...",
 "savollar": [{"savol": "...", "variantlar": ["A","B","C","D"], "togri": 2, "qiyinlik": "oson"}]}
```
`togri` — 0..3 indeks; `qiyinlik` — "oson" | "o'rtacha" | "qiyin".
