import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
records = [
    json.loads(line)
    for line in (ROOT / "audit/qayta_barcha/savollar_holati.jsonl").read_text().splitlines()
    if line.strip()
]

for grade_no in range(3, 10):
    grade = f"{grade_no}-sinf"
    rows = []
    for record in records:
        if record["grade"] != grade or not record.get("source_context_may_be_needed"):
            continue
        question = record["question"]
        rows.append(
            {
                "fan": record["subject"],
                "fayl": record["file"],
                "savol_raqami": record["question_no"],
                "savol": question["savol"],
                "variantlar": " | ".join(question["variantlar"]),
                "belgilangan_javob": question["variantlar"][question["togri"]],
                "holat": "asl matn, rasm, jadval, she’r yoki darslik konteksti bilan tekshirish kerak",
            }
        )
    fields = ["fan", "fayl", "savol_raqami", "savol", "variantlar", "belgilangan_javob", "holat"]
    with (ROOT / grade / "MANBA_TALAB_QILADIGAN_SAVOLLAR.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(grade, len(rows), Counter(row["fan"] for row in rows).most_common(5))
