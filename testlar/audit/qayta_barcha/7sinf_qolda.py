import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "7-sinf/7-sinf 7-Sinf Adabiyot/023_Furqat.json"
data = json.loads(path.read_text())
rows = []
for number, question in enumerate(data["savollar"], 1):
    rows.append(
        {
            "fan": path.parent.name,
            "fayl": str(path.relative_to(ROOT)),
            "savol_raqami": number,
            "muammo_turi": "mavzu va savollar mos emas",
            "savol": question["savol"],
            "belgilangan_javob": question["variantlar"][question["togri"]],
            "izoh": "Fayl va mavzu nomi ‘Furqat’, ammo savollar Abdulla Qodiriy hayoti va asarlari haqida.",
        }
    )
fields = ["fan", "fayl", "savol_raqami", "muammo_turi", "savol", "belgilangan_javob", "izoh"]
with (ROOT / "7-sinf/QOLDA_TASDIQLANGAN_MUAMMOLAR.csv").open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(len(rows))
