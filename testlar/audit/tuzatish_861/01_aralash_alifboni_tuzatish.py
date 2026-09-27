import csv
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BACKUP = ROOT / "audit" / "tuzatish_861" / "zaxira_aralash_alifbo"
JOURNAL = ROOT / "audit" / "tuzatish_861" / "TUZATISHLAR.jsonl"

CYR = "\u0400-\u052f"
LAT = "A-Za-zÀ-ÖØ-öø-ÿʻʼ‘’'"
TOKEN_RE = re.compile(rf"[^\s|]*[{CYR}][^\s|]*")

table = str.maketrans({
    "а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ё":"yo",
    "ж":"j","з":"z","и":"i","й":"y","к":"k","л":"l","м":"m",
    "н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u",
    "ф":"f","х":"x","ц":"ts","ч":"ch","ш":"sh","щ":"sh","ъ":"'",
    "ы":"i","э":"e","ю":"yu","я":"ya","ғ":"g‘","қ":"q","ҳ":"h",
    "ў":"o‘","ј":"j",
    "А":"A","Б":"B","В":"V","Г":"G","Д":"D","Е":"E","Ё":"Yo",
    "Ж":"J","З":"Z","И":"I","Й":"Y","К":"K","Л":"L","М":"M",
    "Н":"N","О":"O","П":"P","Р":"R","С":"S","Т":"T","У":"U",
    "Ф":"F","Х":"X","Ц":"Ts","Ч":"Ch","Ш":"Sh","Щ":"Sh","Ъ":"'",
    "Ы":"I","Э":"E","Ю":"Yu","Я":"Ya","Ғ":"G‘","Қ":"Q","Ҳ":"H",
    "Ў":"O‘","Ј":"J",
})

def translit_mixed_token(token: str) -> str:
    core = token
    if not re.search(rf"[{CYR}]", core) or not re.search(rf"[{LAT}]", core):
        return token
    # Ruscha yumshatish belgisi: Pьеса -> Pyesa; medalь -> medal.
    core = re.sub(r"ь(?=[еёюя])", "y", core, flags=re.I)
    core = core.replace("ь", "").replace("Ь", "")
    return core.translate(table)

def fix_text(text: str) -> str:
    return TOKEN_RE.sub(lambda m: translit_mixed_token(m.group(0)), text)

def load_rows():
    for grade in range(3, 10):
        p = ROOT / f"{grade}-sinf" / "TASDIQLANGAN_ARALASH_ALIFBO.csv"
        if not p.exists():
            continue
        with p.open(encoding="utf-8-sig", newline="") as f:
            yield from csv.DictReader(f)

changes = []
files = {}
for row in load_rows():
    path = ROOT / row["fayl"]
    qno = int(row["savol_raqami"])
    if path not in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        files[path] = data
    data = files[path]
    q = data["savollar"][qno - 1]
    before = {"savol": q["savol"], "variantlar": list(q["variantlar"]), "togri": q["togri"]}
    q["savol"] = fix_text(q["savol"])
    q["variantlar"] = [fix_text(x) for x in q["variantlar"]]
    after = {"savol": q["savol"], "variantlar": list(q["variantlar"]), "togri": q["togri"]}
    if before != after:
        changes.append({
            "vaqt": datetime.now().isoformat(timespec="seconds"),
            "tur": "aralash_alifbo",
            "fayl": row["fayl"],
            "savol_raqami": qno,
            "oldin": before,
            "keyin": after,
            "manba": "TASDIQLANGAN_ARALASH_ALIFBO.csv",
        })

for path, data in files.items():
    rel = path.relative_to(ROOT)
    backup = BACKUP / rel
    backup.parent.mkdir(parents=True, exist_ok=True)
    if not backup.exists():
        shutil.copy2(path, backup)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

JOURNAL.parent.mkdir(parents=True, exist_ok=True)
with JOURNAL.open("a", encoding="utf-8") as f:
    for change in changes:
        f.write(json.dumps(change, ensure_ascii=False) + "\n")

print(f"fayl={len(files)}, tuzatilgan_savol={len(changes)}")
