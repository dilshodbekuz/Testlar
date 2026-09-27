import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
source = ROOT / "6-sinf/ZIDDIYATLI_TAKRORLAR.csv"
rows = list(csv.DictReader(source.open(encoding="utf-8-sig")))

notes = {
    "8": "Bir xil savolga ‘Farg‘ona yaqinidagi kichik qishloqda’ va ‘Katta uyda’ javoblari berilgan; savol yashash joyimi yoki uy turinimi so‘rashi aniqlashtirilsin.",
    "9": "Bir xil ‘qanday joy?’ savoliga ikki turli xususiyat kalit qilingan; savol muayyan faoliyat yoki xususiyatni so‘rashi kerak.",
    "10": "2x+3=x+7 tenglamaning yechimi x=4. 014-mavzudagi ‘3’ kaliti noto‘g‘ri.",
    "11": "‘Ikkita teng nisbatning birlashtirmasi’ proporsiyaning to‘g‘ri ta’rifi emas; birinchi ikki javob mazmunan to‘g‘ri.",
    "12": "Miqdor sonlar tasnifida sanoq, dona, chama, jamlovchi, taqsim va kasr sonlar bo‘ladi; ikkinchi javobda chama son tushib qolgan.",
}

confirmed = []
consistent = []
for row in rows:
    row = dict(row)
    if row["guruh"] in notes:
        row["qo‘lda_izoh"] = notes[row["guruh"]]
        confirmed.append(row)
    else:
        row["qo‘lda_izoh"] = "Javoblar ifodasi farq qiladi, lekin mazmunan bir-biriga zid emas."
        consistent.append(row)

fields = list(rows[0]) + ["qo‘lda_izoh"]
for name, output in (
    ("TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv", confirmed),
    ("MOS_TAKRORIY_JAVOBLAR.csv", consistent),
):
    with (ROOT / "6-sinf" / name).open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
print("tasdiqlangan guruh", len(set(row["guruh"] for row in confirmed)), "mos guruh", len(set(row["guruh"] for row in consistent)))
