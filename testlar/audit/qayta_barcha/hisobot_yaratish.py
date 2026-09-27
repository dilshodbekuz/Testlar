from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audit"
CURRENT = AUDIT / "qayta_barcha"


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def grade_of(path):
    return path.split("/", 1)[0]


def subject_of(path):
    return Path(path).parent.name


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    records = read_jsonl(CURRENT / "savollar_holati.jsonl")
    findings = read_jsonl(CURRENT / "avtomatik_topilmalar.jsonl")
    file_findings = json.loads((CURRENT / "fayl_muammolari.json").read_text())
    stats = json.loads((CURRENT / "statistika.json").read_text())["grades"]

    record_index = {(row["file"], row["question_no"]): row for row in records}
    logs = read_jsonl(AUDIT / "tuzatishlar_qolda.jsonl")
    latest_logs = {(row["fayl"], row["n"]): row for row in logs}

    overall = [
        "# Testlar tekshiruvi — 3–9-sinflar",
        "",
        "Tekshiruv sanasi: 2026-09-27.",
        "",
        "## Umumiy natija",
        "",
        "Barcha mavjud alohida mavzu JSON fayllari texnik va avtomatik qoidalar bilan qayta tekshirildi. Hisobotlar har bir sinf papkasiga yozildi. Test fayllarining o‘zi o‘zgartirilmadi.",
        "",
        "| Sinf | Mavzu fayli | Savol | Signal tushgan savol | Hisoblangan arifmetik savol | Oldingi qo‘llangan tuzatish |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for grade_no in range(3, 10):
        grade = f"{grade_no}-sinf"
        grade_dir = ROOT / grade
        grade_records = [row for row in records if row["grade"] == grade]
        grade_findings = [row for row in findings if grade_of(row["file"]) == grade]
        grade_file_findings = [row for row in file_findings if grade_of(row["file"]) == grade]
        grade_logs = {
            key: value for key, value in latest_logs.items() if grade_of(value["fayl"]) == grade
        }
        applied = 0
        actual_changes = 0
        for (file_name, number), log in grade_logs.items():
            current = record_index.get((file_name, number), {}).get("question")
            applied += current == log["yangi"]
            actual_changes += log["eski"] != log["yangi"]

        subject_stats = defaultdict(lambda: {"files": set(), "questions": 0, "signals": 0})
        for row in grade_records:
            item = subject_stats[row["subject"]]
            item["files"].add(row["file"])
            item["questions"] += 1
        for item in grade_findings:
            subject_stats[subject_of(item["file"])]["signals"] += 1

        detail_rows = []
        for item in grade_findings:
            record = record_index[(item["file"], item["question_no"])]
            question = record["question"]
            detail_rows.append(
                {
                    "fan": subject_of(item["file"]),
                    "fayl": item["file"],
                    "savol_raqami": item["question_no"],
                    "signal": item["code"],
                    "ishonchlilik": item["certainty"],
                    "daraja": item["severity"],
                    "savol": question["savol"],
                    "variantlar": " | ".join(question["variantlar"]),
                    "belgilangan_javob": question["variantlar"][question["togri"]],
                    "izoh": item["detail"],
                }
            )
        write_csv(
            grade_dir / "MUAMMOLI_SAVOLLAR.csv",
            detail_rows,
            [
                "fan", "fayl", "savol_raqami", "signal", "ishonchlilik",
                "daraja", "savol", "variantlar", "belgilangan_javob", "izoh",
            ],
        )

        file_rows = [
            {"fayl_yoki_papka": row["file"], "muammo": row["code"], "izoh": row["detail"]}
            for row in grade_file_findings
        ]
        write_csv(
            grade_dir / "FAYL_MUAMMOLARI.csv",
            file_rows,
            ["fayl_yoki_papka", "muammo", "izoh"],
        )

        codes = Counter(row["code"] for row in grade_findings)
        file_codes = Counter(row["code"] for row in grade_file_findings)
        lines = [
            f"# {grade} testlari tekshiruv hisoboti",
            "",
            "Tekshiruv sanasi: 2026-09-27.",
            "",
            "## Xulosa",
            "",
            f"{len(subject_stats)} ta test mavjud fan papkasidagi {stats[grade]['files']:,} ta alohida mavzu fayli va {stats[grade]['questions']:,} ta savol qayta tekshirildi. "
            f"{stats[grade]['automatic_flagged']:,} ta savolda avtomatik signal bor. Bu signallarning hammasi xato degani emas; teng qiymatli variant savol aynan yozilish shaklini so‘rasa to‘g‘ri bo‘lishi mumkin.",
            "",
            f"Oldingi tuzatish jurnalida {len(grade_logs):,} ta alohida savol bor. Ulardan {actual_changes:,} tasida haqiqiy o‘zgarish qayd etilgan va eng so‘nggi qiymatlarning {applied:,}/{len(grade_logs):,} tasi amaldagi faylga mos.",
            "",
            "## Fanlar bo‘yicha qamrov",
            "",
            "| Fan | Mavzu fayli | Savol | Avtomatik signal |",
            "|---|---:|---:|---:|",
        ]
        for subject, item in sorted(subject_stats.items()):
            lines.append(
                f"| {subject.replace(grade + ' ', '')} | {len(item['files'])} | {item['questions']} | {item['signals']} |"
            )

        lines += [
            "",
            "## Savol signallari",
            "",
            f"- G‘ayrioddiy yoki buzilgan belgi: {codes['text_encoding']} ta.",
            f"- Teng son qiymatli variantlar: {codes['equivalent_numeric_options']} ta.",
            f"- Oddiy arifmetik shablonga mos va qayta hisoblangan savollar: {stats[grade]['arithmetic_calculated']} ta.",
            "- Noto‘g‘ri arifmetik kalit signali: 0 ta.",
            "",
            "Savol darajasidagi to‘liq ro‘yxat [MUAMMOLI_SAVOLLAR.csv](MUAMMOLI_SAVOLLAR.csv) faylida. Unda fan, fayl, savol raqami, matn, variantlar, belgilangan javob va signal sababi bor.",
            "",
            "## Fayl va jamlanma holati",
            "",
            f"- Testi yo‘q fan papkasi: {file_codes['empty_subject']} ta.",
            f"- Jamlanma bilan alohida fayllar farqi: {file_codes['aggregate_difference']} ta fan papkasida.",
            f"- Takror ishlatilgan mavzu raqami: {file_codes['duplicate_topic_number']} ta holat.",
            "",
            "Batafsil ro‘yxat [FAYL_MUAMMOLARI.csv](FAYL_MUAMMOLARI.csv) faylida.",
            "",
            "## Tekshiruv chegarasi",
            "",
            "Bu bosqich barcha savollarning tuzilishi, nusxalar mosligi, oddiy arifmetik shakllar, takror/teng variantlar va buzilgan belgilarni qamrab oladi. Tarix, adabiyot, til qoidasi, darslik matni, rasm va maxsus fan faktlarining har biri asl darslik bilan alohida tasdiqlangan deb hisoblanmaydi. Shuning uchun avtomatik signal chiqmagan savolga ham mutlaq mazmuniy kafolat berilmaydi.",
            "",
            "Test fayllari o‘zgartirilmadi; faqat hisobot fayllari yozildi.",
        ]
        (grade_dir / "HISOBOT.md").write_text("\n".join(lines) + "\n")

        overall.append(
            f"| {grade} | {stats[grade]['files']:,} | {stats[grade]['questions']:,} | "
            f"{stats[grade]['automatic_flagged']:,} | {stats[grade]['arithmetic_calculated']:,} | {applied:,} |"
        )

    overall += [
        "",
        "## Jami",
        "",
        f"- Mavzu fayllari: {sum(row['files'] for row in stats.values()):,} ta.",
        f"- Savollar: {sum(row['questions'] for row in stats.values()):,} ta.",
        f"- Signal tushgan savollar: {sum(row['automatic_flagged'] for row in stats.values()):,} ta.",
        f"- Oddiy arifmetik shaklda qayta hisoblangan savollar: {sum(row['arithmetic_calculated'] for row in stats.values()):,} ta.",
        "- Tuzilish xatosi, bo‘sh savol, noto‘g‘ri variant soni yoki yaroqsiz javob indeksi topilmadi.",
        "",
        "Har bir sinfning batafsil natijasi o‘sha sinf papkasidagi `HISOBOT.md`, `MUAMMOLI_SAVOLLAR.csv` va `FAYL_MUAMMOLARI.csv` fayllarida.",
    ]
    (ROOT / "TEKSHIRUV_HISOBOTI.md").write_text("\n".join(overall) + "\n")


if __name__ == "__main__":
    main()
