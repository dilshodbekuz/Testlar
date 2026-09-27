import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CYRILLIC = re.compile(r"[А-Яа-яЁё]")
LATIN = re.compile(r"[A-Za-z]")
FRAGMENTS = re.compile(r"\S*[А-Яа-яЁё]\S*")


def main():
    for grade_no in range(3, 10):
        grade = f"{grade_no}-sinf"
        rows = []
        for path in sorted((ROOT / grade).glob("*/*.json")):
            if path.name.startswith("_") or "Rus tili" in path.parent.name:
                continue
            try:
                data = json.loads(path.read_text())
            except (ValueError, OSError):
                continue
            if not isinstance(data, dict) or "savollar" not in data:
                continue
            for number, question in enumerate(data["savollar"], 1):
                combined = question.get("savol", "") + " " + " ".join(question.get("variantlar", []))
                if not (CYRILLIC.search(combined) and LATIN.search(combined)):
                    continue
                fragments = sorted(set(FRAGMENTS.findall(combined)))
                rows.append(
                    {
                        "fan": path.parent.name,
                        "fayl": str(path.relative_to(ROOT)),
                        "savol_raqami": number,
                        "savol": question.get("savol", ""),
                        "variantlar": " | ".join(question.get("variantlar", [])),
                        "belgilangan_javob": question["variantlar"][question["togri"]],
                        "kirill_aralash_bolaklar": " | ".join(fragments),
                        "holat": "qo‘lda tekshirish va lotin yozuviga keltirish kerak",
                    }
                )
        target = ROOT / grade / "ARALASH_ALIFBO.csv"
        fields = [
            "fan", "fayl", "savol_raqami", "savol", "variantlar",
            "belgilangan_javob", "kirill_aralash_bolaklar", "holat",
        ]
        with target.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        confirmed = []
        review = []
        for row in rows:
            fragments = row["kirill_aralash_bolaklar"].split(" | ")
            same_token = any(CYRILLIC.search(token) and LATIN.search(token) for token in fragments)
            row = dict(row)
            if same_token:
                row["holat"] = "tasdiqlangan: bitta so‘z ichida kirill va lotin harflari aralashgan"
                confirmed.append(row)
            else:
                row["holat"] = "alohida kirillcha so‘z yoki iqtibos; qo‘lda tekshirish kerak"
                review.append(row)

        for name, output_rows in (
            ("TASDIQLANGAN_ARALASH_ALIFBO.csv", confirmed),
            ("ALOHIDA_KIRILL_SOZLAR.csv", review),
        ):
            with (ROOT / grade / name).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(output_rows)
        print(grade, len(rows), "tasdiqlangan", len(confirmed), "tekshirish", len(review))


if __name__ == "__main__":
    main()
