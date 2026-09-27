import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def normalize(text):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text)).strip().casefold()


def main():
    for grade_no in range(3, 10):
        grade = f"{grade_no}-sinf"
        groups = defaultdict(list)
        for path in sorted((ROOT / grade).glob("*/*.json")):
            if path.name.startswith("_"):
                continue
            try:
                data = json.loads(path.read_text())
            except (ValueError, OSError):
                continue
            if not isinstance(data, dict) or "savollar" not in data:
                continue
            for number, question in enumerate(data["savollar"], 1):
                groups[(path.parent.name, normalize(question["savol"]))].append((path, number, question))

        duplicate_rows = []
        conflict_rows = []
        group_no = 0
        conflict_no = 0
        for (_, _), entries in sorted(groups.items()):
            if len(entries) < 2:
                continue
            group_no += 1
            answers = {normalize(question["variantlar"][question["togri"]]) for _, _, question in entries}
            if len(answers) > 1:
                conflict_no += 1
            for path, number, question in entries:
                row = {
                    "guruh": group_no,
                    "fan": path.parent.name,
                    "fayl": str(path.relative_to(ROOT)),
                    "savol_raqami": number,
                    "savol": question["savol"],
                    "variantlar": " | ".join(question["variantlar"]),
                    "belgilangan_javob": question["variantlar"][question["togri"]],
                    "holat": "bir xil savol matni boshqa fayl/savolda ham mavjud",
                }
                duplicate_rows.append(row)
                if len(answers) > 1:
                    conflict = dict(row)
                    conflict["guruh"] = conflict_no
                    conflict["holat"] = "bir xil savol matniga turli belgilangan javob berilgan; qo‘lda tekshirish kerak"
                    conflict_rows.append(conflict)

        fields = ["guruh", "fan", "fayl", "savol_raqami", "savol", "variantlar", "belgilangan_javob", "holat"]
        for name, rows in (
            ("TAKRORIY_SAVOLLAR.csv", duplicate_rows),
            ("ZIDDIYATLI_TAKRORLAR.csv", conflict_rows),
        ):
            with (ROOT / grade / name).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        print(grade, "takror guruh", group_no, "ziddiyat guruh", conflict_no)


if __name__ == "__main__":
    main()
