import csv
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[2]
src = root / "7-sinf" / "ZIDDIYATLI_TAKRORLAR.csv"
with src.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

groups = defaultdict(list)
for row in rows:
    groups[int(row["guruh"])].append(row)

# 4-guruhda aynan bir xil va kontekstsiz savol ikki boshqa tushunchani
# (quvvatning ta'rifi va skalyarligi) so'rayotgandek kalitlangan.
confirmed = {4}

def write(name, selected, note):
    out = root / "7-sinf" / name
    fields = list(rows[0]) + ["qolda_xulosa"]
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for group_no in sorted(selected):
            for row in groups[group_no]:
                w.writerow({**row, "qolda_xulosa": note[group_no]})

write(
    "TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv",
    confirmed,
    {4: "Bir xil kontekstsiz savol ikki xil mezon bo'yicha kalitlangan: biri quvvat ta'rifi, biri skalyar kattalik ekanini so'raydi. Savol matni aniqlashtirilishi kerak."},
)

consistent = set(groups) - confirmed
write(
    "MOS_TAKRORIY_JAVOBLAR.csv",
    consistent,
    {n: "Javoblar mazmunan mos yoki savol matnidagi 'matnga ko'ra' kabi ibora alohida mavzu kontekstiga bog'liq; bevosita javob ziddiyati tasdiqlanmadi." for n in consistent},
)

print(f"tasdiqlangan={len(confirmed)}, mos/kontekstga_bogliq={len(consistent)}")
