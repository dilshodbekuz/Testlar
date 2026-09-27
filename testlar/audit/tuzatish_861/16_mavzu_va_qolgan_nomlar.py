#!/usr/bin/env python3
"""Kitob bilan tasdiqlangan mavzu/fayl nomlari va qolgan buzilgan matnlarni tuzatadi."""
from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audit" / "tuzatish_861"
BACKUP = AUDIT / "zaxira_mavzu_nomlari"
JOURNAL = AUDIT / "TUZATISHLAR.jsonl"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def backup(path: Path) -> None:
    dst = BACKUP / path.relative_to(ROOT)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not dst.exists():
        shutil.copy2(path, dst)


def log(path: Path, number, before, after, reason: str) -> None:
    row = {
        "vaqt": datetime.now().isoformat(timespec="seconds"),
        "fayl": str(path.relative_to(ROOT)),
        "savol_raqami": number,
        "oldin": before,
        "keyin": after,
        "sabab": reason,
        "manba": "tegishli sinf darsligi PDF",
    }
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# 7-sinf adabiyot: 250-betdan boshlanadigan bo'lim Abdulla Qodiriy haqida.
adab = ROOT / "7-sinf" / "7-sinf 7-Sinf Adabiyot"
old_json = adab / "023_Furqat.json"
new_json = adab / "023_Abdulla Qodiriy.json"
old_txt = adab / "023_Furqat.txt"
new_txt = adab / "023_Abdulla Qodiriy.txt"
if old_json.exists():
    backup(old_json)
    backup(old_txt)
    data = load(old_json)
    before = data.get("mavzu")
    data["mavzu"] = "Abdulla Qodiriy"
    save(new_json, data)
    old_json.unlink()
    if old_txt.exists():
        old_txt.unlink()  # sinxronlash skripti yangisini JSON asosida yaratadi
    log(new_json, "mavzu", before, data["mavzu"], "Fayldagi 30 savol va darslik bo'limi Abdulla Qodiriyga tegishli")

mavzular = adab / "_mavzular.json"
data = load(mavzular)
for item in data:
    if item.get("mavzu") == "Furqat" and item.get("bosh") == 250:
        backup(mavzular)
        before = item["mavzu"]
        item["mavzu"] = "Abdulla Qodiriy"
        save(mavzular, data)
        log(mavzular, "mavzu", before, item["mavzu"], "Darslikdagi 250-bet bo'limiga moslashtirildi")
        break

# 6-sinf geografiya mavzusi: buzilgan eski ð belgisi faqat nomlarda qolgan.
geo = ROOT / "6-sinf" / "6-sinf 6-Sinf Geografiya"
old_geo = geo / "006_6- §. Mobilizm giðotezasi.json"
new_geo = geo / "006_6- §. Mobilizm gipotezasi.json"
if old_geo.exists():
    backup(old_geo)
    data = load(old_geo)
    before = data.get("mavzu")
    data["mavzu"] = "6- §. Mobilizm gipotezasi"
    save(new_geo, data)
    old_geo.unlink()
    old_geo.with_suffix(".txt").unlink(missing_ok=True)
    log(new_geo, "mavzu", before, data["mavzu"], "Buzilgan 'giðoteza' yozuvi 'gipoteza'ga tuzatildi")

geo_topics = geo / "_mavzular.json"
data = load(geo_topics)
changed = False
for item in data:
    if "giðoteza" in item.get("mavzu", ""):
        backup(geo_topics)
        before = item["mavzu"]
        item["mavzu"] = before.replace("giðoteza", "gipoteza")
        log(geo_topics, "mavzu", before, item["mavzu"], "Buzilgan belgi tuzatildi")
        changed = True
if changed:
    save(geo_topics, data)

# 6-sinf rus tili: mojibake jumla kitobdagi ruscha gapga qaytarildi.
rus = ROOT / "6-sinf" / "6-sinf 6-Sinf Rus tili" / "007_Глаголы совершенного и несовершенного вида.json"
data = load(rus)
q = data["savollar"][11]
before = q["savol"]
after = '«Я вскопал крупную грядку» jumlasida fe’lning qaysi turi ishlatilgan?'
if before != after:
    backup(rus)
    q["savol"] = after
    q["variantlar"] = ["Несовершенный вид", "Совершенный вид", "Ikkalasi ham", "Hech biri"]
    q["togri"] = 1
    save(rus, data)
    log(rus, 12, before, q, "Buzilgan ruscha gap va grammatik atamalar tiklandi")

print("Mavzu nomlari va qolgan buzilgan jumla tuzatildi.")
