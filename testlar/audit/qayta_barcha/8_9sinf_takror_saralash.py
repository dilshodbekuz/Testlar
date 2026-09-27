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
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for number in sorted(selected):
                for row in groups[number]:
                    w.writerow({**row, "qolda_xulosa": notes[number]})

    confirmed = set(confirmed_notes)
    write("TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv", confirmed, confirmed_notes)
    consistent = set(groups) - confirmed
    write(
        "MOS_TAKRORIY_JAVOBLAR.csv",
        consistent,
        {n: "Javoblar mazmunan teng/mos yoki savol alohida mavzu, matn yoxud laboratoriya ishi kontekstiga bog'liq; bevosita ziddiyat tasdiqlanmadi." for n in consistent},
    )
    print(f"{grade}-sinf: tasdiqlangan={len(confirmed)}, mos/kontekstga_bogliq={len(consistent)}")

process(8, {})
process(9, {
    3: "Bir xil kontekstsiz savol y=x³ funksiyaning ikki boshqa xossasiga ('o'suvchi' va 'toq') kalitlangan; qaysi xossa so'ralgani aniqlashtirilishi kerak.",
    4: "AABB gomozigot genotip faqat AB gameta hosil qiladi; '2 xil' deb kalitlangan takror ziddiyatli.",
    5: "AaBb genotip to'rt xil gameta (AB, Ab, aB, ab) hosil qiladi; faqat AB va aB deb kalitlangan takror ziddiyatli.",
    6: "Aynan bir xil AaBb genotipli tovuq uchun ikki xil toj shakli kalitlangan; ikkala javob bir vaqtda to'g'ri bo'la olmaydi.",
    7: "Aynan bir xil iiCC genotipli tovuq pati uchun 'rangli' va 'oq' javoblari qarama-qarshi kalitlangan.",
})
