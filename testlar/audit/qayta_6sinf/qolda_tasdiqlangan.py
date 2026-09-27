import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRADE = ROOT / "6-sinf"


def get(prefix, topic_prefix, number):
    folder = next(path for path in GRADE.iterdir() if path.is_dir() and prefix in path.name)
    path = next(folder.glob(topic_prefix + "*.json"))
    data = json.loads(path.read_text())
    return path, data, data["savollar"][number - 1]


def make_row(path, number, question, kind, note):
    return {
        "fan": path.parent.name,
        "fayl": str(path.relative_to(ROOT)),
        "savol_raqami": number,
        "muammo_turi": kind,
        "savol": question["savol"],
        "variantlar": " | ".join(question["variantlar"]),
        "belgilangan_javob": question["variantlar"][question["togri"]],
        "izoh": note,
    }


def main():
    rows = []
    fixed = [
        ("Geografiya", "003_", 19, "noto‘g‘ri kalit va buzilgan matn", "Eng sodda organizmlar geografik qobiq rivojiga ta’sir ko‘rsatgan; belgilangan ‘sezilarli o‘zgarish keltirmadi’ javobi mazmunga zid."),
        ("Geografiya", "005_", 10, "noto‘g‘ri kalit", "Abissal mintaqa 3000–6000 m chuqurlikda; A varianti mos, D kalit noto‘g‘ri."),
        ("Geografiya", "005_", 15, "to‘g‘ri variant yo‘q", "Batial mintaqa odatda 200–3000 m oralig‘i; variantlarda bu oraliq yo‘q, D kalit abissal mintaqaga mos."),
        ("Rus tili", "007_", 12, "o‘qib bo‘lmaydigan savol", "‘Ã vskopalkrupnuypartipok’ matni buzilgan; fe’l turini aniqlashning iloji yo‘q."),
    ]
    for subject, topic, number, kind, note in fixed:
        path, _, question = get(subject, topic, number)
        rows.append(make_row(path, number, question, kind, note))

    path, data, _ = get("Geografiya", "006_", 1)
    for number, question in enumerate(data["savollar"], 1):
        combined = question["savol"] + " " + " ".join(question["variantlar"])
        if "giðotez" in combined:
            rows.append(make_row(path, number, question, "tizimli imlo buzilishi", "‘giðoteza’/‘giðotezasi’ so‘zi ‘gipoteza’/‘gipotezasi’ bo‘lishi kerak."))

    path, data, _ = get("Rus tili", "008_", 1)
    for number, question in enumerate(data["savollar"], 1):
        rows.append(make_row(path, number, question, "yozuv tizimi nomuvofiqligi", "Ruscha misollar saqlanishi mumkin, ammo o‘zbekcha savol va izohlar boshqa mavzulardagi kabi lotin yozuvida berilishi kerak."))

    fields = ["fan", "fayl", "savol_raqami", "muammo_turi", "savol", "variantlar", "belgilangan_javob", "izoh"]
    with (GRADE / "QOLDA_TASDIQLANGAN_MUAMMOLAR.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(len(rows))


if __name__ == "__main__":
    main()
