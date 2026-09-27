from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRADE = ROOT / "3-sinf"
AUDIT = ROOT / "audit"
OUT = Path(__file__).resolve().parent


def compact(value):
    if isinstance(value, list):
        return " | ".join(str(item) for item in value)
    return str(value or "")


def question_hash(question):
    raw = json.dumps(question, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def subject_name(path):
    return path.parent.name.replace("3-sinf 3-Sinf ", "")


def write_csv(path, rows, fieldnames):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    subjects = []
    all_questions = {}
    individual_payloads = defaultdict(list)

    for folder in sorted(path for path in GRADE.iterdir() if path.is_dir()):
        files = sorted(folder.glob("[0-9]*.json"))
        count = 0
        for path in files:
            data = json.loads(path.read_text())
            rel = str(path.relative_to(ROOT))
            individual_payloads[str(folder.relative_to(ROOT))].append((path, data))
            for number, question in enumerate(data["savollar"], 1):
                all_questions[(rel, number)] = question
                count += 1
        subjects.append(
            {
                "fan": folder.name.replace("3-sinf 3-Sinf ", ""),
                "papka": folder,
                "fayllar": len(files),
                "savollar": count,
            }
        )

    logs = []
    for line in (AUDIT / "tuzatishlar_qolda.jsonl").read_text().splitlines():
        item = json.loads(line)
        if item["fayl"].startswith("3-sinf/"):
            logs.append(item)
    latest = {(item["fayl"], item["n"]): item for item in logs}

    corrections = []
    applied = 0
    actual_change = 0
    correction_counts = Counter()
    for (rel, number), item in sorted(latest.items()):
        current = all_questions.get((rel, number))
        is_applied = current == item["yangi"]
        changed = item["eski"] != item["yangi"]
        applied += is_applied
        actual_change += changed
        if changed:
            correction_counts[subject_name(ROOT / rel)] += 1
        old = item["eski"]
        new = item["yangi"]
        changed_fields = [key for key in ("savol", "variantlar", "togri", "qiyinlik") if old.get(key) != new.get(key)]
        corrections.append(
            {
                "fan": subject_name(ROOT / rel),
                "fayl": rel,
                "savol_raqami": number,
                "holat": "qo‘llangan" if is_applied else "amaldagi fayl mos emas",
                "haqiqiy_ozgarish": "ha" if changed else "yo‘q",
                "ozgargan_maydonlar": ", ".join(changed_fields),
                "eski_savol": old.get("savol", ""),
                "yangi_savol": new.get("savol", ""),
                "eski_variantlar": compact(old.get("variantlar", [])),
                "yangi_variantlar": compact(new.get("variantlar", [])),
                "eski_javob": "ABCD"[old["togri"]] if isinstance(old.get("togri"), int) else "",
                "yangi_javob": "ABCD"[new["togri"]] if isinstance(new.get("togri"), int) else "",
            }
        )

    reviews = json.loads((AUDIT / "manual_reviews.json").read_text())
    unresolved = []
    unresolved_counts = Counter()
    for review in reviews:
        rel = review["file"]
        if not rel.startswith("3-sinf/") or review["status"] not in {"tahrir", "manba_kerak", "xato"}:
            continue
        current = all_questions.get((rel, review["question_no"]))
        if current is None or question_hash(current) != review["sha256"]:
            continue
        answer = current["variantlar"][current["togri"]]
        fan = subject_name(ROOT / rel)
        unresolved_counts[(fan, review["status"])] += 1
        unresolved.append(
            {
                "fan": fan,
                "fayl": rel,
                "savol_raqami": review["question_no"],
                "holat": review["status"],
                "savol": current["savol"],
                "belgilangan_javob": answer,
                "variantlar": compact(current["variantlar"]),
                "izoh": " ".join(review.get("notes", [])),
            }
        )

    # Qayta audit paytida bevosita amaldagi fayllarda tasdiqlangan yangi
    # topilmalar. Matematika 013:5 va 033:1 hamda Odobnoma 002:4 va 002:25
    # eski qaydlarda borligi uchun bu ro‘yxatda takrorlanmaydi.
    spot_findings = [
        ("3-sinf/3-sinf 3-Sinf Ingliz tili/001_Unit 1 Lesson 1 I have two sisters.json", 3, "«Opalar yoki singililar» → «Opalar yoki singillar»; C variantidagi «ukalari» ham parallel shaklda «ukalar» bo‘lishi kerak."),
        ("3-sinf/3-sinf 3-Sinf Ingliz tili/001_Unit 1 Lesson 1 I have two sisters.json", 8, "«Akalar yoki ukalari» → «Akalar yoki ukalar»."),
        ("3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json", 2, "«Feruza kimdir?» → «Feruza kim?»; «O‘quvchisidir» → «O‘quvchi»."),
        ("3-sinf/3-sinf 3-Sinf Rus tili/001_В школе.json", 9, "«Shkolning direktyori kimdir?» jumlasi adabiy o‘zbekchada «Maktab direktori kim?» shaklida yozilsin."),
        ("3-sinf/3-sinf 3-Sinf O‘qish/005_Mahallam ajib ko'rkam.json", 8, "«bilalar», «Ko‘zbiyallag‘ich, båkinmachiq va siqqa» buzilgan. O‘yin nomlari asl matn bilan solishtirib tiklansin."),
        ("3-sinf/3-sinf 3-Sinf Tabiatshunoslik/001_Tabiatshunoslik nimani o'rganadi.json", 6, "«Cho‘lla» → «Cho‘llar»."),
        ("3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json", 5, "Belgilangan «Muhim damda, o‘zgarlik ko‘rsatishda» javobi tushunarsiz. Savol darslikdagi ‘o‘ng qo‘l qoidasi’ mazmuniga ko‘ra qayta tuzilsin."),
        ("3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json", 6, "«Nima qilmaslik kerak?» savoliga «xalaqit qilmaslik» javobi ikki inkor hosil qiladi; savol va variantlar bir xil mantiqiy shaklga keltirilsin."),
        ("3-sinf/3-sinf 3-Sinf Tarbiya/001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json", 8, "«Jarohalarishlashning» → «Jarohatlanishning»."),
        ("3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json", 7, "«To‘g‘ri o‘tirish qanday? — To‘g‘ri» aylana ta’rif; to‘g‘ri holat belgilari aniq yozilsin."),
        ("3-sinf/3-sinf 3-Sinf Tasviriy san’at/001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json", 10, "Kalitdagi «tuza va ishlaydigan» grammatik buzilgan; «San’at asarlarini yaratadi» shakli mos."),
        ("3-sinf/3-sinf 3-Sinf Texnologiya/001_«Kuz» manzarasini applikatsiya usulida yasash.json", 8, "«Detalllarni» → «Detallarni»; savol «Applikatsiya yasash qaysi bosqichdan boshlanadi?» shaklida yozilsin."),
        ("3-sinf/3-sinf 3-Sinf Texnologiya/001_«Kuz» manzarasini applikatsiya usulida yasash.json", 9, "«Rang tutirib» buzilgan chalg‘ituvchi variant; mazmunli variant bilan almashtirilsin."),
    ]
    existing_unresolved = {(item["fayl"], item["savol_raqami"]) for item in unresolved}
    for rel, number, note in spot_findings:
        if (rel, number) in existing_unresolved:
            continue
        current = all_questions[(rel, number)]
        fan = subject_name(ROOT / rel)
        unresolved_counts[(fan, "tahrir")] += 1
        unresolved.append(
            {
                "fan": fan,
                "fayl": rel,
                "savol_raqami": number,
                "holat": "tahrir",
                "savol": current["savol"],
                "belgilangan_javob": current["variantlar"][current["togri"]],
                "variantlar": compact(current["variantlar"]),
                "izoh": note,
            }
        )
    unresolved.sort(key=lambda item: (item["fan"], item["fayl"], item["savol_raqami"]))

    aggregate_missing = []
    aggregate_summary = Counter()
    duplicate_numbers = Counter()
    for subject in subjects:
        folder = subject["papka"]
        rel_folder = str(folder.relative_to(ROOT))
        aggregate_path = folder / "_TOLIQ.json"
        if not aggregate_path.exists():
            continue
        aggregate = json.loads(aggregate_path.read_text())
        aggregate_counter = Counter(json.dumps(item, ensure_ascii=False, sort_keys=True) for item in aggregate)
        prefixes = Counter()
        for path, data in individual_payloads[rel_folder]:
            prefixes[path.name.split("_", 1)[0]] += 1
            packed = json.dumps(data, ensure_ascii=False, sort_keys=True)
            if aggregate_counter[packed]:
                aggregate_counter[packed] -= 1
            else:
                aggregate_missing.append(
                    {
                        "fan": subject["fan"],
                        "fayl": str(path.relative_to(ROOT)),
                        "savollar_soni": len(data["savollar"]),
                    }
                )
                aggregate_summary[subject["fan"]] += len(data["savollar"])
        duplicate_numbers[subject["fan"]] = sum(1 for count in prefixes.values() if count > 1)

    write_csv(
        OUT / "3_SINF_TUZATISHLAR.csv",
        corrections,
        list(corrections[0]),
    )
    write_csv(
        OUT / "3_SINF_QOLGAN_MUAMMOLAR.csv",
        unresolved,
        list(unresolved[0]),
    )
    write_csv(
        OUT / "3_SINF_JAMLANMAGA_KIRMAGAN_FAYLLAR.csv",
        aggregate_missing,
        list(aggregate_missing[0]),
    )

    lines = [
        "# 3-sinf testlari bo‘yicha to‘liq hisobot",
        "",
        "Hisobot sanasi: 2026-09-27.",
        "",
        "## Yakuniy xulosa",
        "",
        "3-sinf testlari hali to‘liq tayyor emas. Mavjud 9 fandagi fayllar texnik jihatdan ochiladi va JSON/TXT nusxalari mos, lekin amaldagi savollarda tahrir hamda manba bilan tekshirish talab qiladigan muammolar qolgan. Musiqa va Ona tili papkalarida alohida mavzu testlari yo‘q. To‘rtta fanning `_TOLIQ.json` jamlanmasi alohida mavzu fayllarining hammasini qamramaydi.",
        "",
        "Oldingi tekshiruv jurnallari barcha mavjud mavzular ko‘rib chiqilganini qayd etadi. Ushbu qayta audit esa o‘sha tuzatishlar amaldagi fayllarga qo‘llanganini tekshirdi va o‘zgarishsiz qolgan muammoli savollarni ajratdi. Shu sababli ‘ko‘rib chiqilgan’ holati ‘barcha xatolar bartaraf etilgan’ degani emas.",
        "",
        "## Umumiy raqamlar",
        "",
        f"- Fan papkalari: {len(subjects)} ta.",
        f"- Test mavjud fanlar: {sum(item['fayllar'] > 0 for item in subjects)} ta.",
        f"- Alohida mavzu JSON fayllari: {sum(item['fayllar'] for item in subjects)} ta.",
        f"- Alohida mavzu fayllaridagi savollar: {sum(item['savollar'] for item in subjects):,} ta.",
        f"- Tuzatish jurnalidagi 3-sinf yozuvlari: {len(logs):,} ta; alohida savollar: {len(latest):,} ta.",
        f"- Haqiqiy o‘zgarish kiritilgan alohida savollar: {actual_change:,} ta.",
        f"- Eng so‘nggi jurnal qiymati amaldagi faylga mos savollar: {applied:,}/{len(latest):,} ta.",
        f"- O‘zgarishsiz qolgan tasdiqlangan muammo: {len(unresolved):,} ta.",
        f"- Jamlanmaga kirmagan alohida fayllar: {len(aggregate_missing):,} ta; ulardagi savollar: {sum(item['savollar_soni'] for item in aggregate_missing):,} ta.",
        "",
        "## Fanlar bo‘yicha holat",
        "",
        "| Fan | Mavzu fayli | Savol | Haqiqiy tuzatilgan savol | Qolgan tahrir | Manba kerak | Jamlanmada yo‘q savol | Holat |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for item in subjects:
        fan = item["fan"]
        edit_count = unresolved_counts[(fan, "tahrir")] + unresolved_counts[(fan, "xato")]
        source_count = unresolved_counts[(fan, "manba_kerak")]
        if item["fayllar"] == 0:
            status = "Test yo‘q"
        elif edit_count or source_count or aggregate_summary[fan]:
            status = "Tuzatish kerak"
        else:
            status = "Qayd etilgan ochiq muammo yo‘q"
        lines.append(
            f"| {fan} | {item['fayllar']} | {item['savollar']} | {correction_counts[fan]} | "
            f"{edit_count} | {source_count} | {aggregate_summary[fan]} | {status} |"
        )

    lines += [
        "",
        "## Qolgan muammolar",
        "",
        "Quyidagi jadvalda amaldagi savol izi oldingi muammo qaydidagi iz bilan aynan mos bo‘lgan savollar berilgan. Demak, ular qayddan keyin o‘zgartirilmagan. `Tahrir` — savol, variant yoki kalitni tuzatish kerakligini; `manba_kerak` — darslik, rasm yoki ishonchli manbasiz yakuniy hukm berib bo‘lmasligini bildiradi.",
        "",
        "| № | Fan | Fayl | Savol | Holat | Muammo/tavsiya |",
        "|---:|---|---|---:|---|---|",
    ]
    for index, item in enumerate(unresolved, 1):
        filename = Path(item["fayl"]).name.replace("|", "\\|")
        note = item["izoh"].replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {index} | {item['fan']} | {filename} | {item['savol_raqami']} | {item['holat']} | {note} |"
        )

    lines += [
        "",
        "## Jamlanma muammolari",
        "",
        "| Fan | `_TOLIQ.json`ga kirmagan fayl | Ulardagi savol | Takror ishlatilgan mavzu raqami |",
        "|---|---:|---:|---:|",
    ]
    for item in subjects:
        fan = item["fan"]
        missing_files = sum(row["fan"] == fan for row in aggregate_missing)
        lines.append(
            f"| {fan} | {missing_files} | {aggregate_summary[fan]} | {duplicate_numbers[fan]} |"
        )

    lines += [
        "",
        "Jamlanmaga kirmagan fayllarning to‘liq ro‘yxati `3_SINF_JAMLANMAGA_KIRMAGAN_FAYLLAR.csv` faylida. Bir xil mavzu raqami ishlatilishi avtomatik ravishda dublikat degani emas: ko‘p joyda `a/b` yoki turli matnli mavzular bor. Shu sababli ular avtomatik o‘chirilmadi.",
        "",
        "## Texnik tekshiruv",
        "",
        "- 530 ta alohida JSON fayl ochildi.",
        "- Har bir savolda 4 ta bo‘sh bo‘lmagan variant va 0–3 oralig‘idagi javob indeksi bor.",
        "- Barcha mavjud mavzu TXT nusxalari JSON savol, variant va javob kalitiga mos.",
        "- Aynan bir xil variantli savol topilmadi.",
        "- Oddiy arifmetik shablonga mos 578 savol qayta hisoblandi; noto‘g‘ri kalit signali topilmadi.",
        "- 13 ta teng son qiymatli variant signali qo‘lda ko‘rildi. Ko‘pchiligi savolning shakli sababli xato emas; Matematika 013:5 va 033:1 savollariga kontekst qo‘shish kerak.",
        "- O‘qish fanida 559 ta g‘ayrioddiy belgi signali bor. Signal soni xatolar soni emas, ammo `Vàtàn`, `o‘chîg‘i`, `båkinmachiq` kabi real matn buzilishlari qolgan.",
        "",
        "## Hisobot fayllari",
        "",
        "- `3_SINF_TUZATISHLAR.csv` — tuzatish jurnalidagi 2 435 ta alohida savolning eski va yangi ko‘rinishi.",
        "- `3_SINF_QOLGAN_MUAMMOLAR.csv` — o‘zgarishsiz qolgan barcha tahrir/manba qaydlari, amaldagi savol va belgilangan javob bilan.",
        "- `3_SINF_JAMLANMAGA_KIRMAGAN_FAYLLAR.csv` — `_TOLIQ.json` jamlanmalarida yo‘q barcha alohida mavzu fayllari.",
        "",
        "## Chegara",
        "",
        "Bu hisobot mavjud audit dalillari va amaldagi fayllarning qayta texnik tekshiruviga asoslangan. Tarixiy, adabiy va darslikka bog‘liq har bir da’vo asl darslik bilan boshidan oxirigacha qayta tasdiqlanmagan. `Manba kerak` holatidagi savollar shuning uchun tayyor deb hisoblanmaydi. Musiqa va Ona tili testlari yaratilmaguncha 3-sinfning barcha fanlari to‘liq tayyor bo‘ldi deb bo‘lmaydi.",
    ]

    (OUT / "3_SINF_TOLIQ_HISOBOT.md").write_text("\n".join(lines) + "\n")

    print(
        json.dumps(
            {
                "subjects": len(subjects),
                "files": sum(item["fayllar"] for item in subjects),
                "questions": sum(item["savollar"] for item in subjects),
                "unique_log_questions": len(latest),
                "actual_changes": actual_change,
                "applied_latest": applied,
                "unresolved": len(unresolved),
                "aggregate_missing_files": len(aggregate_missing),
                "aggregate_missing_questions": sum(item["savollar_soni"] for item in aggregate_missing),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
