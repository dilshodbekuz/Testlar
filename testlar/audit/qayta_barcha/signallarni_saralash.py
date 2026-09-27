import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def classification(grade, row):
    code = row["signal"]
    file_name = row["fayl"]
    number = row["savol_raqami"]

    if grade == 5:
        if code == "text_encoding":
            return "tasdiqlangan matn xatosi", "`Milân` yozuvi `Milan` shaklida yozilishi kerak."
        return "xato emas", "Savol aynan xona yozuvi, amal yoki ifoda shaklini so‘raydi; kalit bir ma’noli."
    if grade == 6:
        if code == "text_encoding":
            return "tasdiqlangan matn xatosi", "So‘zdagi g‘ayrioddiy belgi matn buzilishidir."
        if "011_Nisbat tushunchasi" in file_name and number == "19":
            return "tasdiqlangan ko‘p javobli savol", "2:3, 4:6 va 6:9 nisbatlari teng; uchta variant to‘g‘ri."
        return "xato emas", "Savol tub yoyilma, eng sodda nisbat yoki tegishli darajani so‘ragani uchun kalit ajraladi."
    if grade == 7:
        if code == "text_encoding":
            return "xato emas", "Å — angstrom o‘lchov birligining to‘g‘ri belgisi."
        return "xato emas", "Yil oralig‘i son ifodasi sifatida signal bergan; savol va kalit bir ma’noli."
    if grade == 8:
        return "xato emas", "Adèle — fransuzcha ismning to‘g‘ri yozilishi."
    if grade == 9:
        return "xato emas", "O‘xshash shakllar yuzlari nisbati chiziqli nisbatning kvadratiga teng; kalit to‘g‘ri."
    raise ValueError(grade)


def main():
    for grade in range(5, 10):
        folder = ROOT / f"{grade}-sinf"
        source = folder / "MUAMMOLI_SAVOLLAR.csv"
        with source.open(encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
        fields = list(rows[0]) + ["yakuniy_holat", "yakuniy_izoh"] if rows else []
        confirmed = []
        rejected = []
        for row in rows:
            state, note = classification(grade, row)
            row["yakuniy_holat"] = state
            row["yakuniy_izoh"] = note
            (rejected if state == "xato emas" else confirmed).append(row)

        target = folder / "TASDIQLANGAN_MUAMMOLAR.csv"
        with target.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(confirmed)

        rejected_target = folder / "XATO_EMAS_SIGNALLAR.csv"
        with rejected_target.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rejected)

        print(grade, "tasdiqlangan", len(confirmed), "xato emas", len(rejected))


if __name__ == "__main__":
    main()
