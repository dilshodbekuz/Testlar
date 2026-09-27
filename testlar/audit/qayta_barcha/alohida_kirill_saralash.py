import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

# Alohida kirillcha tokenlar orasidan kontekstda lotin yozuvida bo‘lishi aniq
# bo‘lganlari. Dastur interfeysidagi ruscha menyu nomlari va mahsulot nomlari
# bu ro‘yxatga kiritilmaydi.
CONFIRMED = {
    5: {
        ("5-sinf/5-sinf 5-Sinf Ingliz tili/010_UNIT 10 Wildlife.json", "19"),
        ("5-sinf/5-sinf 5-Sinf Musiqa/019_6-dars. Musiqali drama.json", "29"),
        ("5-sinf/5-sinf 5-Sinf Tarixdan hikoyalar/005_Qoyatosh suratlari.json", "9"),
    },
    6: {
        ("6-sinf/6-sinf 6-Sinf Adabiyot (2-qism)/010_Tog'ay Murod.json", "24"),
        ("6-sinf/6-sinf 6-Sinf Fizika/014_Paskal qonuni va uning qo'llanilishi.json", "4"),
        ("6-sinf/6-sinf 6-Sinf Fizika/014_Paskal qonuni va uning qo'llanilishi.json", "10"),
        ("6-sinf/6-sinf 6-Sinf Geografiya/024_26- §. Materik aholisi va uning tabiatga ta'siri.json", "23"),
    },
    7: {
        ("7-sinf/7-sinf 7-Sinf Adabiyot/005_Mardlik afsonasi.json", "27"),
    },
}


def main():
    for grade in range(3, 10):
        source = ROOT / f"{grade}-sinf" / "ALOHIDA_KIRILL_SOZLAR.csv"
        with source.open(encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
            fields = handle.seek(0) or []
        fieldnames = list(rows[0]) if rows else [
            "fan", "fayl", "savol_raqami", "savol", "variantlar",
            "belgilangan_javob", "kirill_aralash_bolaklar", "holat",
        ]
        confirmed = []
        remaining = []
        selected = CONFIRMED.get(grade, set())
        for row in rows:
            if (row["fayl"], row["savol_raqami"]) in selected:
                row["holat"] = "tasdiqlangan: lotin yozuvidagi savolda aloqasiz kirillcha so‘z"
                confirmed.append(row)
            else:
                remaining.append(row)
        for name, output in (
            ("TASDIQLANGAN_ALOHIDA_KIRILL.csv", confirmed),
            ("TEKSHIRILADIGAN_KIRILL_IQTIBOSLAR.csv", remaining),
        ):
            with (ROOT / f"{grade}-sinf" / name).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(output)
        print(grade, "tasdiqlangan", len(confirmed), "qolgan", len(remaining))


if __name__ == "__main__":
    main()
