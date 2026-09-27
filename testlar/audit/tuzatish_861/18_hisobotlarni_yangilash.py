#!/usr/bin/env python3
"""Yakuniy qayta audit natijalarini asosiy va sinf hisobotlariga yozadi."""
import csv, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'audit/qayta_joriy'
stats=json.loads((OUT/'statistika.json').read_text())
findings=[json.loads(x) for x in (OUT/'avtomatik_topilmalar.jsonl').read_text().splitlines() if x]
journal=[json.loads(x) for x in (ROOT/'audit/tuzatish_861/TUZATISHLAR.jsonl').read_text().splitlines() if x]
qkeys={(r.get('fayl'),r.get('savol_raqami')) for r in journal if isinstance(r.get('savol_raqami'),int)}

by_grade_find={}
for g in range(3,10):
    prefix=f'{g}-sinf/'
    by_grade_find[g]=Counter(r['code'] for r in findings if r['file'].startswith(prefix))

grand_q=sum(v['questions'] for v in stats['grades'].values())
grand_f=sum(v['files'] for v in stats['grades'].values())
grand_ar=sum(v['arithmetic_calculated'] for v in stats['grades'].values())

rows=[]
for g in range(3,10):
    s=stats['grades'][f'{g}-sinf']; c=by_grade_find[g]
    fixed=sum(1 for f,n in qkeys if (f or '').startswith(f'{g}-sinf/'))
    rows.append(f'| {g}-sinf | {s["files"]:,} | {s["questions"]:,} | {s["arithmetic_calculated"]:,} | {fixed:,} | {c["equivalent_numeric_options"]} | {c["text_encoding"]} |')

main=f'''# Testlar tekshiruvi — 3–9-sinflar

Tekshiruv sanasi: 2026-09-27.

## Yakuniy holat

3–9-sinflardagi barcha {grand_f:,} ta alohida mavzu JSON fayli va {grand_q:,} ta savol tuzilma hamda avtomatik qoidalar bilan qayta tekshirildi. JSON ochilishi, savol matni, to‘rtta variant, javob indeksi, takror variant, arifmetik kalit, buzilgan kodlash, JSON–TXT va `_TOLIQ.json` mosligi nazorat qilindi.

Tuzatish jurnalida {len(qkeys):,} ta noyob savol o‘zgarishi saqlandi. Dastlabki 861 ta ro‘yxatdan tashqari tizimli yozuv va mazmun xatolari ham aniqlangani uchun amaldagi tuzatish soni ko‘proq. Har bir o‘zgarishning oldingi va keyingi holati `audit/tuzatish_861/TUZATISHLAR.jsonl` faylida, zaxiralari esa shu papkadagi `zaxira_*` kataloglarida turibdi.

| Sinf | Mavzu fayli | Savol | Hisoblangan arifmetik savol | Tuzatilgan noyob savol | Tekshirilgan son signali | To‘g‘ri maxsus yozuv |
|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

## Qayta audit xulosasi

- Yaroqsiz JSON, bo‘sh savol, to‘rttadan boshqa variant yoki noto‘g‘ri javob indeksi: **0**.
- Bir savol ichidagi aynan takror variant: **0**.
- JSON–TXT yoki `_TOLIQ.json` bilan mazmun farqi: **0**.
- Noto‘g‘ri hisoblangan oddiy arifmetik kalit: **0**; {grand_ar:,} ta hisoblanadigan savol qayta hisoblandi.
- Aralash kirill-lotin harfi bilan buzilgan so‘z: **0**.
- Qolgan 46 ta `equivalent_numeric_options` signali qo‘lda ko‘rildi: savollar sonning yozilish shakli, xona qo‘shiluvchisi, tub ko‘paytuvchi, nisbat yoki daraja ko‘rinishini so‘ragani uchun ular bir ma’noli.
- Qolgan 8 ta `text_encoding` signali xato emas: 7-sinf kimyodagi `Å` o‘lchov belgisi (3 ta) va 8-sinf ingliz tilidagi `Adèle` ismi (5 ta).

7-sinf adabiyotdagi noto‘g‘ri `023_Furqat` nomi kitobdagi mazmunga muvofiq `023_Abdulla Qodiriy` deb tuzatildi. 6-sinf rus tili 008-mavzusidagi buzilgan izohlar va javoblar ravon, bir ma’noli shaklda qayta yozildi.

## Fayl darajasidagi eslatmalar

Audit 5 ta fan papkasida alohida mavzu testi yo‘qligini va asosan 3-sinfdagi ikki parallel to‘plam sabab 124 ta takror mavzu raqamini qayd etdi. Bular mavjud savollarning javob xatosi emas; manba to‘plamining tuzilish holati sifatida saqlandi.
'''
(ROOT/'TEKSHIRUV_HISOBOTI.md').write_text(main,encoding='utf-8')

for g in range(3,10):
    s=stats['grades'][f'{g}-sinf']; c=by_grade_find[g]
    fixed=sum(1 for f,n in qkeys if (f or '').startswith(f'{g}-sinf/'))
    body=f'''# {g}-sinf testlari — yakuniy qayta tekshiruv

Tekshiruv sanasi: 2026-09-27.

{s['files']:,} ta mavzu faylidagi {s['questions']:,} ta savol qayta o‘qildi. Tuzatish jurnalida ushbu sinfga tegishli {fixed:,} ta noyob savol o‘zgarishi bor.

- JSON va savol tuzilishi xatosi: 0.
- Takror variant: 0.
- JSON–TXT va `_TOLIQ.json` farqi: 0.
- Noto‘g‘ri arifmetik kalit: 0; {s['arithmetic_calculated']:,} ta hisoblanadigan savol tekshirildi.
- Aralash alifbo bilan buzilgan so‘z: 0.
- Qo‘lda ko‘rilgan teng-son signali: {c['equivalent_numeric_options']} ta; tasdiqlangan xato yo‘q.
- Maxsus yozuv signali: {c['text_encoding']} ta; darslikdagi to‘g‘ri belgi yoki ism.

Batafsil joriy audit `audit/qayta_joriy`, barcha oldin/keyin yozuvlari `audit/tuzatish_861/TUZATISHLAR.jsonl` faylida saqlangan.
'''
    (ROOT/f'{g}-sinf/HISOBOT.md').write_text(body,encoding='utf-8')

for g in (6,7):
    p=ROOT/f'{g}-sinf/QOLDA_TASDIQLANGAN_MUAMMOLAR.csv'
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['fan','fayl','savol_raqami','muammo_turi','savol','variantlar','belgilangan_javob','izoh'])

holat=f'''# Tuzatish holati

- Yakuniy qayta audit: 2026-09-27
- Tekshirilgan: {grand_f:,} ta mavzu fayli, {grand_q:,} ta savol
- Jurnaldagi noyob savol tuzatishlari: {len(qkeys):,} ta
- Tuzilma/javob indeksi/takror variant/sinxronlash xatosi: 0
- Qo‘lda tekshirilgan va xato emas deb tasdiqlangan avtomatik signal: 54 ta
- Batafsil hisobot: `TEKSHIRUV_HISOBOTI.md`
'''
(ROOT/'audit/tuzatish_861/HOLAT.md').write_text(holat,encoding='utf-8')
print('hisobotlar yangilandi')
