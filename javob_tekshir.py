"""Tayyor testlarning javob kalitlarini tekshirib, xatolarini tuzatadi.

Har bir mavzu fayli alohida qisqa `claude -p` so'rov bilan tekshiriladi:
model faqat xato savollarni qaytaradi (noto'g'ri kalit yoki to'g'ri javobi
yo'q / bir nechta bo'lgan savol). Tuzatishlar .json, .txt va _TOLIQ.json ga
yoziladi, eski-yangi holati testlar/audit/javob_tuzatishlar.jsonl da saqlanadi.
Tekshirilgan fayllar qayta tekshirilmaydi (ish qolgan joydan davom etadi).

    python javob_tekshir.py 3-sinf          # bitta sinf / fan
    python javob_tekshir.py --holat 3-sinf  # progress
"""
import hashlib
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import test_generator as tg

MODEL = "sonnet"                 # kalitni tekshirishda aniqlik muhim
PARALLEL = 3
AUDIT = tg.NATIJA_PAPKASI / "audit"
HOLAT = AUDIT / "javob_tekshiruv_holati.json"
JURNAL = AUDIT / "javob_tuzatishlar.jsonl"
_QULF = threading.Lock()

PROMPT = """Siz {sinf} o'qituvchisisiz. "{kitob}" fanidan "{mavzu}" mavzusidagi test savollarini tekshiring.
Har bir savolda "Kalit" - hozir to'g'ri deb belgilangan variant.

Faqat XATO savollarni qaytaring:
- kalit noto'g'ri, lekin variantlar orasida bitta aniq to'g'ri javob bor ->
  {{"n": 5, "togri": "C", "sabab": "qisqa izoh"}}
- to'g'ri javob umuman yo'q, bir nechta variant to'g'ri, yoki shart yetarli emas ->
  savolni tuzating (mavzu va qiyinlik o'zgarmasin, 4 ta har xil variant, bittasi aniq to'g'ri):
  {{"n": 5, "savol": "...", "variantlar": ["...", "...", "...", "..."], "togri": "B", "sabab": "qisqa izoh"}}

Hisob-kitoblarni diqqat bilan qayta hisoblang. Faqat aniq ishonchingiz komil bo'lsa o'zgartiring;
darslikka bog'liq, tekshirib bo'lmaydigan savollarga tegmang. Hammasi to'g'ri bo'lsa: []
Javob - faqat JSON massiv.

SAVOLLAR:
{savollar}"""


def iz(yol):
    return hashlib.sha1(yol.read_bytes()).hexdigest()[:16]


def holat_ol():
    try:
        return json.loads(HOLAT.read_text(encoding="utf-8"))
    except Exception:
        return {}


def holat_yoz(h):
    tmp = HOLAT.with_suffix(".tmp")
    tmp.write_text(json.dumps(h, ensure_ascii=False, indent=0), encoding="utf-8")
    tmp.replace(HOLAT)


def savollar_matni(savollar):
    q = []
    for i, s in enumerate(savollar, 1):
        q.append(f"{i}. {s['savol']}")
        q += [f"{'ABCD'[j]}) {v}" for j, v in enumerate(s["variantlar"])]
        q += [f"Kalit: {'ABCD'[s['togri']]}", ""]
    return "\n".join(q)


def harf(x):
    x = str(x).strip().upper()[:1]
    return "ABCD".index(x) if x and x in "ABCD" else None


def tuzat(yol, holat):
    kalit = str(yol.relative_to(tg.NATIJA_PAPKASI))
    if holat.get(kalit) == iz(yol):
        return 0
    d = json.loads(yol.read_text(encoding="utf-8"))
    sv = d["savollar"]
    javob = tg.claude(PROMPT.format(sinf=d.get("sinf", ""), kitob=d.get("kitob", ""),
                                    mavzu=d.get("mavzu", ""), savollar=savollar_matni(sv)),
                      model=MODEL)
    try:
        tuzatishlar = tg.json_ol(javob)
    except Exception:
        raise tg.ClaudeXato("JSON o'qilmadi: " + javob[-200:])

    ozgardi = []
    for t in tuzatishlar:
        try:
            i = int(t["n"]) - 1
            yangi_t = harf(t["togri"])
            if not (0 <= i < len(sv)) or yangi_t is None:
                continue
            eski = dict(sv[i], variantlar=list(sv[i]["variantlar"]))
            if t.get("variantlar"):
                v = [str(x).strip() for x in t["variantlar"]]
                if len(v) != 4 or len(set(v)) != 4 or not str(t.get("savol", "")).strip():
                    continue
                sv[i]["savol"], sv[i]["variantlar"] = str(t["savol"]).strip(), v
            elif yangi_t == sv[i]["togri"]:
                continue
            sv[i]["togri"] = yangi_t
            ozgardi.append({"fayl": kalit, "n": i + 1, "sabab": t.get("sabab", ""),
                            "eski": eski, "yangi": sv[i]})
        except Exception:
            continue

    if ozgardi:
        yol.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        tg.txt_yoz(yol.with_suffix(".txt"), d["mavzu"], sv)
        with _QULF, JURNAL.open("a", encoding="utf-8") as f:
            for o in ozgardi:
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
    with _QULF:
        holat[kalit] = iz(yol)
        holat_yoz(holat)
    tg.yoz(f"  {'*' if ozgardi else ' '} {kalit}: {len(ozgardi)} tuzatish")
    return len(ozgardi)


def toliq_yangila(papka):
    fayllar = sorted(papka.glob("[0-9]*.json"))
    birlashgan = [json.loads(f.read_text(encoding="utf-8")) for f in fayllar]
    (papka / "_TOLIQ.json").write_text(json.dumps(birlashgan, ensure_ascii=False, indent=1),
                                       encoding="utf-8")


def fayllar(args):
    hammasi = sorted((p for p in tg.NATIJA_PAPKASI.rglob("[0-9]*.json")
                      if "audit" not in p.parts), key=tg.tartib)
    if args:
        hammasi = [p for p in hammasi
                   if any(a.lower() in str(p.relative_to(tg.NATIJA_PAPKASI)).lower() for a in args)]
    return hammasi


def aylanish(royxat, holat):
    """"tayyor" | "limit" | "toxta" qaytaradi."""
    papkalar = {}
    for p in royxat:
        papkalar.setdefault(p.parent, []).append(p)
    nosoz = False
    for papka, ps in papkalar.items():
        tg.yoz(f"[{papka.relative_to(tg.NATIJA_PAPKASI)}]")
        jami = 0
        with ThreadPoolExecutor(PARALLEL) as ex:
            ishlar = [ex.submit(tuzat, p, holat) for p in ps]
            for ish in ishlar:
                try:
                    jami += ish.result()
                except tg.LimitTugadi:
                    return "limit"
                except tg.KirishYoq as e:
                    tg.yoz("Claude Code'ga kirilmagan (`claude` -> /login).", e)
                    return "toxta"
                except Exception as e:
                    tg.yoz(f"  ! {e}")
                    nosoz = True
        if jami:
            toliq_yangila(papka)
    return "nosoz" if nosoz else "tayyor"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    royxat = fayllar(args)
    holat = holat_ol()
    if "--holat" in sys.argv:
        tayyor = sum(1 for p in royxat
                     if holat.get(str(p.relative_to(tg.NATIJA_PAPKASI))) == iz(p))
        tuz = sum(1 for _ in JURNAL.open(encoding="utf-8")) if JURNAL.exists() else 0
        print(f"Tekshirildi: {tayyor}/{len(royxat)} mavzu; jami tuzatishlar (jurnal): {tuz}")
        return
    print(f"{len(royxat)} ta mavzu fayli\n")
    while True:
        n = aylanish(royxat, holat)
        if n == "tayyor":
            print("\nHammasi tekshirildi!")
            return
        if n == "toxta" or "--bir-marta" in sys.argv:
            return
        print("\nLimit/nosozlik - 1 daqiqadan keyin davom etadi.")
        time.sleep(tg.KUTISH_DAQIQA * 60)


if __name__ == "__main__":
    main()
