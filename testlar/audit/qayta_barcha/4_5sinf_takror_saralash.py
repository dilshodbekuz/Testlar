import csv
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[2]

def process(grade, confirmed_notes):
    src = root / f"{grade}-sinf" / "ZIDDIYATLI_TAKRORLAR.csv"
    with src.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    groups = defaultdict(list)
    for row in rows:
        groups[int(row["guruh"])].append(row)
    fields = list(rows[0]) + ["qolda_xulosa"]
    def write(name, selected, notes):
        with (root / f"{grade}-sinf" / name).open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
            for n in sorted(selected):
                for row in groups[n]: w.writerow({**row, "qolda_xulosa": notes[n]})
    confirmed = set(confirmed_notes)
    write("TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv", confirmed, confirmed_notes)
    consistent = set(groups) - confirmed
    write("MOS_TAKRORIY_JAVOBLAR.csv", consistent, {n: "Javoblar mazmunan teng/mos yoki alohida asar va hudud kontekstiga bog'liq; bevosita ziddiyat tasdiqlanmadi." for n in consistent})
    print(f"{grade}-sinf: tasdiqlangan={len(confirmed)}, mos/kontekstga_bogliq={len(consistent)}")

process(4, {})
process(5, {
    8: "Bir xil savolga ikki farqli ta'rif berilgan; birinchi ta'rif fayllarni hisobga olmay, papkani faqat papka va ostki kataloglarning umumiy nomi deb noto'liq ifodalaydi.",
    19: "Bir xil savol uchun 'silindrsimon to'g'rilash moslamasi' va 'silindrsimon po'lat omburlar' turlicha asbob sifatida kalitlangan; termin/asbob aniqlashtirilishi kerak.",
})
