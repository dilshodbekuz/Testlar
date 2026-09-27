import csv
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[2]
src = root / "3-sinf" / "ZIDDIYATLI_TAKRORLAR.csv"
with src.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
groups = defaultdict(list)
for row in rows:
    groups[int(row["guruh"])].append(row)

notes = {
    3: "Ladybird uchun 'Serangga' (o'zbekcha atama emas) va 'Insekt' kalitlari ishlatilgan; javob o'zbekcha 'xonqizi hasharoti' kabi aniqlashtirilishi kerak.",
    4: "Motorbike ta'riflaridan birida 'ikki g'altakli transport' yozilgan; bu 'ikki g'ildirakli' so'zining xatosi.",
    6: "Unit 14 mavzusi aynan bir xil savolda 'Cartoons' va 'Qissalarning dunyosi' deb ikki xil kalitlangan.",
    16: "'Laylak qor' muallifi aynan bir xil savolda Orif To'xtash va Sà'dullàyåvà deb ikki xil kalitlangan.",
    49: "Natyurmort ishlashning birinchi bosqichi kuzatish/savollarga javob topish va tasvirni qog'ozga joylashtirish deb turlicha kalitlangan; bosqich mezoni aniqlashtirilishi kerak.",
    53: "Rasm ishlashning oxirgi bosqichi 'tasvirni aniqlashtirish' va 'tasvirni bo'yash' deb turlicha kalitlangan; savol mavzu yoki bosqichlar ketma-ketligini ko'rsatmaydi.",
    54: "Rasm ishlashning oxirgi bosqichi 'aniq tasvirni ishlash' va 'bo'yoqlar bilan ishlov berish' deb turlicha kalitlangan; savol mavzu yoki bosqichlar ketma-ketligini ko'rsatmaydi.",
}
fields = list(rows[0]) + ["qolda_xulosa"]
def write(name, selected, messages):
    with (root / "3-sinf" / name).open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for n in sorted(selected):
            for row in groups[n]: w.writerow({**row, "qolda_xulosa": messages[n]})
write("TASDIQLANGAN_ZIDDIYATLI_TAKRORLAR.csv", set(notes), notes)
consistent = set(groups) - set(notes)
write("MOS_TAKRORIY_JAVOBLAR.csv", consistent, {n: "Javoblar mazmunan teng/mos yoki alohida dars, she'r, matn va loyiha kontekstiga bog'liq; bevosita ziddiyat tasdiqlanmadi." for n in consistent})
print(f"tasdiqlangan={len(notes)}, mos/kontekstga_bogliq={len(consistent)}")
