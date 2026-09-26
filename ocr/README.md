# Skaner PDF -> matnli PDF (OCR)

Ba'zi darsliklar rasmga olingan (skaner) PDF — ichida matn yo'q, shuning uchun
`test_generator.py` ularni o'tkazib yuboradi. Bu papkadagi vosita macOS'ning
o'z OCR'idan (Vision framework) foydalanib matnni o'qiydi. Hech qanday
kutubxona o'rnatish shart emas, model limiti ham ishlatilmaydi.

## Ishlatish

Bir marta kompilyatsiya qiling:

    swiftc -O ocr/ocr.swift -o ocr/ocr

Keyin har bir kitob uchun:

    cp "kitoblar/9-sinf/<kitob>.pdf" "skaner_asl/9-sinf/<kitob>.pdf"
    python3 ocr/ocr_quvur.py "skaner_asl/9-sinf/<kitob>.pdf" "kitoblar/9-sinf/<kitob>.pdf"

Asl skaner nusxa `skaner_asl/` da qoladi, `kitoblar/` ga matnli PDF tushadi.
Sahifa raqamlari 1:1 saqlanadi, shuning uchun mavzu sahifa oraliqlari buzilmaydi.
Tezligi: ~160 sahifa 1 daqiqada.

## Muhim: qaysi kitoblarga yaramaydi

Formulali fanlarda OCR formulalarni buzadi (`x²` -> `x*`, kasrlar aralashadi),
shuning uchun bu fanlar OCR qilinmadi:

- 8-sinf Algebra, Fizika, Chizmachilik
- 9-sinf Algebra, Fizika

Matnli fanlarda (tarix, adabiyot, biologiya, botanika, til) sifat yaxshi.

## OCR qilingan kitoblar (2026-09-26)

3-sinf Ingliz tili · 4-sinf Ingliz tili · 6-sinf Botanika ·
8-sinf Adabiyot · 8-sinf Biologiya · 8-sinf O'zbekiston tarixi ·
9-sinf Jahon tarixi

Bu 7 kitobdan test HALI yaratilmagan.
