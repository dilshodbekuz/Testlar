import csv
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BACKUP = ROOT / "audit" / "tuzatish_861" / "zaxira_maxsus_belgilar"
JOURNAL = ROOT / "audit" / "tuzatish_861" / "TUZATISHLAR.jsonl"

# Faqat qo'lda tasdiqlangan satrlarda, kontekstga xos almashtirishlar.
rules = {
    "Syrdårya": "Sirdaryo", "shå'riy": "she'riy", "Ò": "T",
    "Machtà": "Machta", "Milân": "Milan", "Tåmirchi": "Temirchi",
    "Birinñhi": "Birinchi", "Uñh": "Uch", "uõhinchi": "uchinchi",
    "uõh": "uch", "ðarta": "marta", "anña": "ancha", "qadamña": "qadamcha",
}

sources = []
for grade in (4, 5, 6):
    p = ROOT / f"{grade}-sinf" / "TASDIQLANGAN_MUAMMOLAR.csv"
    if p.exists():
        with p.open(encoding="utf-8-sig", newline="") as f: sources.extend(csv.DictReader(f))

files = {}; changes=[]
def apply(text):
    for a,b in rules.items(): text=text.replace(a,b)
    return text

for row in sources:
    path=ROOT/row['fayl']; qno=int(row['savol_raqami'])
    data=files.setdefault(path,json.loads(path.read_text(encoding='utf-8')))
    q=data['savollar'][qno-1]
    before={"savol":q['savol'],"variantlar":list(q['variantlar']),"togri":q['togri']}
    q['savol']=apply(q['savol']); q['variantlar']=[apply(x) for x in q['variantlar']]
    after={"savol":q['savol'],"variantlar":list(q['variantlar']),"togri":q['togri']}
    if before!=after:
        changes.append({"vaqt":datetime.now().isoformat(timespec='seconds'),"tur":"maxsus_belgi","fayl":row['fayl'],"savol_raqami":qno,"oldin":before,"keyin":after,"manba":"TASDIQLANGAN_MUAMMOLAR.csv"})

for path,data in files.items():
    rel=path.relative_to(ROOT); backup=BACKUP/rel; backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists(): shutil.copy2(path,backup)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with JOURNAL.open('a',encoding='utf-8') as f:
    for x in changes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(f'fayl={len(files)}, tuzatilgan_savol={len(changes)}')
