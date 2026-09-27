import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "4-sinf" / "MUAMMOLI_SAVOLLAR.csv"
TARGET = ROOT / "4-sinf" / "TASDIQLANGAN_MUAMMOLAR.csv"

# Teng qiymatli variant signallaridan faqat shu savolda bir nechta javob
# savol talabiga ham birday mos keladi. Qolgan to‘rtta savol xona
# qo‘shiluvchilarining to‘liq yozilishini so‘raydi.
AMBIGUOUS = {
    (
        "4-sinf/4-sinf 4-Sinf Matematika/007_Qo'shishning o'rin almashtirish va guruhlash xossasi.json",
        "5",
    )
}


def main():
    with SOURCE.open(encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    source_fields = list(rows[0])

    confirmed = []
    rejected = []
    for row in rows:
        key = (row["fayl"], row["savol_raqami"])
        if row["signal"] == "text_encoding":
            row["yakuniy_holat"] = "tasdiqlangan matn xatosi"
            row["yakuniy_izoh"] = "G‘ayrioddiy belgi so‘zning buzilgan yozuvida ishlatilgan."
            confirmed.append(row)
        elif key in AMBIGUOUS:
            row["yakuniy_holat"] = "tasdiqlangan ko‘p javobli savol"
            row["yakuniy_izoh"] = "To‘rtta variantning ham qiymati 1800; bitta to‘g‘ri javob ajralmaydi."
            confirmed.append(row)
        else:
            row["yakuniy_holat"] = "xato emas"
            row["yakuniy_izoh"] = "Son qiymatlari teng bo‘lsa ham, faqat kalit savolda talab qilingan to‘liq xona yozuviga mos."
            rejected.append(row)

    fields = source_fields + ["yakuniy_holat", "yakuniy_izoh"]
    with TARGET.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(confirmed)

    (ROOT / "audit" / "qayta_4sinf" / "rad_etilgan_signallar.json").write_text(
        json.dumps(rejected, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"tasdiqlangan": len(confirmed), "xato_emas": len(rejected)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
