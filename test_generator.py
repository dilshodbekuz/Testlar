# -*- coding: utf-8 -*-
"""
test_generator.py - maktab darsliklari (PDF) dan har bir mavzu bo'yicha
10 ta oson + 10 ta o'rtacha + 10 ta qiyin test yaratadi.

Tuzilma:
    kitoblar/3-sinf/Matematika.pdf ...  ->  testlar/3-sinf/Matematika/001_<mavzu>.json + .txt

Buyruqlar:
    python test_generator.py              # hamma kitoblar
    python test_generator.py 7-sinf       # faqat nomida "7-sinf" bo'lganlar (fan nomi ham bo'ladi)
    python test_generator.py --holat      # progress: qaysi kitob qancha tayyor
Limit tugasa dastur to'xtaydi; qayta ishga tushirilsa qolgan joyidan davom etadi.
"""
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# ================== SOZLAMALAR ==================
ASOSIY = Path(__file__).resolve().parent
KITOBLAR_PAPKASI = ASOSIY / "kitoblar"
NATIJA_PAPKASI = ASOSIY / "testlar"
BACKEND = "claude_code"          # "claude_code" yoki "api"
# claude_code uchun model. Kichik sinflarda savollar sodda - "haiku" yetarli va
# limitni ancha tejaydi. Katta sinflarda "qiyin" savollar ko'p qadamli fikrlashni
# talab qiladi, u yerda "haiku" savollarni bir xil qolipda chiqaradi.
# Ikkalasini ham bir xil qilmoqchi bo'lsangiz - ikkala qatorga bir xil nom yozing.
CLAUDE_MODEL = "haiku"           # 3 - 6-sinflar uchun
KATTA_SINF_MODEL = "sonnet"      # 7-sinf va undan yuqorisi uchun ("opus" kuchliroq)
KATTA_SINF = 7                   # shu sinfdan boshlab KATTA_SINF_MODEL ishlatiladi
API_MODEL = "claude-sonnet-4-5"  # faqat "api" uchun; joriy nomini docs.claude.com dan tekshiring
SAVOL_SONI = 30                  # 3 ga bo'linadigan son bo'lsin (oson/o'rtacha/qiyin teng)
MAX_MATN = 40000                 # bitta mavzu uchun yuboriladigan matn uzunligi (belgi)
YETARLI_FARQ = 2                 # 30 o'rniga 28 ta chiqsa ham qabul qilinadi (qayta so'rov qimmat)
PARALLEL = 5                     # bir vaqtda nechta mavzu ishlansin (1 = ketma-ket)
# ================================================

DARAJALAR = ["oson", "o'rtacha", "qiyin"]

# claude_code uchun qisqa tizim prompti. Claude Code'ning o'z tizim prompti va
# tool ta'riflari ~39 000 token tutadi; bu yerda ular kerak emas, shuning uchun
# --tools "" va --system-prompt bilan almashtiriladi (~1 100 tokenga tushadi).
TIZIM_PROMPT = ("Siz o'zbek maktabining tajribali o'qituvchisisiz. "
                "Sizdan so'ralgan JSON ma'lumotni qaytaring - "
                "izoh, sarlavha yoki kod bloki belgisisiz, faqat JSON.")

TEJAMKOR_BAYROQLAR = ["--tools", "",
                      "--system-prompt", TIZIM_PROMPT,
                      "--strict-mcp-config",
                      "--setting-sources", "",
                      "--no-session-persistence"]
TEJAMKOR = True                  # ishlamasa dastur o'zi False ga o'tkazadi

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


class LimitTugadi(Exception):
    pass


_CHOP = threading.Lock()         # parallel oqimlar yozuvi aralashmasligi uchun
TOXTA = threading.Event()        # limit tugasa - qolganlari darrov to'xtaydi


def yoz(*a):
    with _CHOP:
        print(*a, flush=True)


MAVZU_PROMPT = """Quyida darslikning har bir PDF sahifasining boshlang'ich qismi berilgan.
Darslikdagi barcha mavzularni (dars / paragraf) tartib bilan aniqlang.
Mundarija, so'zboshi, javoblar va ilovalarni mavzu sifatida olmang.
Faqat JSON massiv qaytaring, boshqa hech narsa yozmang:
[{"mavzu": "mavzu nomi", "bosh": 12, "oxir": 15}]
bosh / oxir - "=== SAHIFA N ===" belgisidagi N raqamlari.

"""

TEST_PROMPT = """Siz tajribali o'qituvchisiz. Quyidagi {sinf} darslik matni asosida "{mavzu}" mavzusi bo'yicha
aynan {n} ta test savoli tuzing (o'zbek tilida, lotin yozuvida, shu sinf o'quvchisi darajasida).
Talablar:
- har bir savolda 4 ta variant, faqat bittasi to'g'ri
- savollar faqat shu matndagi bilimga asoslansin va takrorlanmasin
- qiyinlik bo'yicha teng bo'ling: aynan {k} ta "oson", {k} ta "o'rtacha", {k} ta "qiyin"
  oson - ta'rif, qoida, faktni bilish; o'rtacha - bir qadamli qo'llash;
  qiyin - bir necha qadamli fikrlash yoki bilimlarni birlashtirish
- rasmsiz tushunib bo'lmaydigan savol tuzmang
- hisob-kitobli savollarda javobni ikki marta tekshiring
Faqat JSON massiv qaytaring, boshqa hech narsa yozmang:
[{{"savol": "...", "variantlar": ["...", "...", "...", "..."], "togri": 0, "qiyinlik": "oson"}}]
("togri" - to'g'ri variant indeksi, 0 dan 3 gacha)

MATN:
{matn}"""


def model_tanla(sinf):
    """"7-sinf" kabi nomdan raqamni ajratib, mos modelni qaytaradi."""
    raqam = re.match(r"\s*(\d+)", str(sinf))
    if raqam and int(raqam.group(1)) >= KATTA_SINF:
        return KATTA_SINF_MODEL
    return CLAUDE_MODEL


def claude(prompt, model=None):
    model = model or CLAUDE_MODEL
    if BACKEND == "api":
        import anthropic
        r = anthropic.Anthropic().messages.create(
            model=API_MODEL, max_tokens=16000,
            messages=[{"role": "user", "content": prompt}])
        return "".join(b.text for b in r.content if b.type == "text")

    exe = shutil.which("claude")
    if not exe:
        sys.exit("`claude` buyrug'i topilmadi. Claude Code o'rnatilganini tekshiring.")
    # Kompyuterda ANTHROPIC_API_KEY bo'lsa, Claude Code obuna o'rniga API kreditni ishlatadi.
    # Shuning uchun uni olib tashlaymiz - faqat claude.ai obunangiz ishlatiladi.
    env = {k: v for k, v in os.environ.items()
           if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}
    model_bayrogi = ["--model", model] if model else []

    # 1-urinish: tokenni tejaydigan bayroqlar bilan (tool ta'riflari, MCP
    # serverlar, sozlama fayllari va uzun standart tizim prompti yuborilmaydi -
    # bitta so'rov ~39 500 token o'rniga ~1 100 tokenga tushadi).
    # 2-urinish: agar ular ishlamasa (eski Claude Code versiyasi yoki Windows'da
    # bo'sh matnli bayroq muammosi) - oddiy usulda, dastur to'xtab qolmasin.
    global TEJAMKOR
    urinishlar = [TEJAMKOR_BAYROQLAR + model_bayrogi] if TEJAMKOR else []
    urinishlar.append(model_bayrogi)

    oxirgi = None
    for n, qoshimcha in enumerate(urinishlar):
        r = subprocess.run([exe, "-p"] + qoshimcha, input=prompt,
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=1200,
                           cwd=tempfile.gettempdir(), env=env)
        out = r.stdout or ""
        oxirgi = (out + (r.stderr or ""))[-500:]
        if r.returncode == 0 and out.strip():
            return out
        if re.search(r"limit|usage", oxirgi, re.I) and len(out) < 400:
            raise LimitTugadi(oxirgi)      # limit tugagan - qayta urinish behuda
        if n == 0 and len(urinishlar) > 1:
            TEJAMKOR = False               # boshqa mavzularda ham urinib o'tirmaymiz
            yoz("    ! tejamkor rejim bu kompyuterda ishlamadi - oddiy rejimga o'tildi")
    raise LimitTugadi(oxirgi)


def json_ol(matn):
    a, b = matn.find("["), matn.rfind("]")
    return json.loads(matn[a:b + 1])


def sahifalar(pdf):
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(str(pdf))
    return [doc[i].get_textpage().get_text_range().replace("\r", "") for i in range(len(doc))]


def tekshir(savollar):
    yaxshi, korilgan = [], set()
    for s in savollar:
        try:
            v, t, q = s["variantlar"], int(s["togri"]), s["savol"].strip()
            d = str(s.get("qiyinlik", "")).lower().replace("‘", "'").replace("’", "'")
            s["qiyinlik"] = next((x for x in DARAJALAR if x in d), "o'rtacha")
            if len(v) == 4 and 0 <= t < 4 and q and q not in korilgan:
                korilgan.add(q)
                togri = v[t]
                random.shuffle(v)          # to'g'ri javob doim A bo'lib qolmasin
                s["togri"] = v.index(togri)
                yaxshi.append(s)
        except Exception:
            pass
    return yaxshi


def darajala(savollar):
    k = SAVOL_SONI // 3
    natija = []
    for d in DARAJALAR:
        natija += [s for s in savollar if s["qiyinlik"] == d][:k]
    return natija


def yetarlimi(savollar):
    # Bitta-ikkita savol yetmasa ham qabul qilamiz: butun so'rovni qaytadan
    # yuborish bitta savolga arzimaydi.
    return len(savollar) >= SAVOL_SONI - YETARLI_FARQ


def txt_yoz(yol, mavzu, savollar):
    q = [mavzu, ""]
    oldingi = None
    for i, s in enumerate(savollar, 1):
        if s["qiyinlik"] != oldingi:
            oldingi = s["qiyinlik"]
            q += [f"--- {oldingi.upper()} ---", ""]
        q.append(f"{i}. {s['savol']}")
        for j, v in enumerate(s["variantlar"]):
            q.append(f"{'+' if j == s['togri'] else ''}{'ABCD'[j]}) {v}")
        q.append("")
    yol.write_text("\n".join(q), encoding="utf-8")


def natija_papkasi(pdf):
    return NATIJA_PAPKASI / pdf.relative_to(KITOBLAR_PAPKASI).with_suffix("")


def fayl_nomi(k, mavzu):
    nom = re.sub(r'[\\/:*?"<>|\n\r\t]', "", mavzu)[:60].strip()
    return f"{k:03d}_{nom}"


def kitob(pdf):
    papka = natija_papkasi(pdf)
    papka.mkdir(parents=True, exist_ok=True)
    sinf = pdf.relative_to(KITOBLAR_PAPKASI).parts[0]
    model = model_tanla(sinf)
    pages = sahifalar(pdf)
    if sum(len(p.strip()) for p in pages) < 2000:
        print("  ! matn topilmadi (skaner PDF?) - o'tkazildi")
        return

    mf = papka / "_mavzular.json"
    if mf.exists():
        mavzular = json.loads(mf.read_text(encoding="utf-8"))
    else:
        xarita = "\n".join(f"=== SAHIFA {i + 1} ===\n{p.strip()[:250]}" for i, p in enumerate(pages))
        # Mavzularni ajratish oddiy ish - eng arzon model bilan.
        mavzular = json_ol(claude(MAVZU_PROMPT + xarita, CLAUDE_MODEL))
        mf.write_text(json.dumps(mavzular, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {len(mavzular)} ta mavzu (model: {model})")

    def bitta_mavzu(k, m):
        """Bitta mavzuni to'liq ishlaydi. Parallel oqimlarda chaqiriladi."""
        if TOXTA.is_set():
            return
        jf = papka / (fayl_nomi(k, m["mavzu"]) + ".json")
        if jf.exists():
            return
        bosh = max(1, int(m["bosh"]))
        oxir = max(bosh, int(m["oxir"]))
        matn = "\n".join(pages[bosh - 1:oxir])[:MAX_MATN]

        savollar = []
        for _ in range(2):  # yetarli chiqmasa bir marta qayta urinadi
            try:
                javob = claude(TEST_PROMPT.format(sinf=sinf, mavzu=m["mavzu"], n=SAVOL_SONI,
                                                  k=SAVOL_SONI // 3, matn=matn), model)
                yangi = darajala(tekshir(json_ol(javob)))
            except LimitTugadi:
                TOXTA.set()            # qolgan oqimlar ham to'xtasin
                raise
            except Exception as e:
                yoz(f"    xato: {e}")
                continue
            if len(yangi) > len(savollar):
                savollar = yangi
            if yetarlimi(savollar):
                break
        if not savollar:
            yoz(f"    ! [{k}] {m['mavzu']} - o'tkazildi")
            return

        # Fayl to'liq yozilishiga ishonch: avval vaqtinchalik nomga, keyin ko'chiramiz.
        # Aks holda dastur to'xtab qolsa yarim fayl "tayyor" deb hisoblanardi.
        vaqt = jf.with_suffix(".yozilmoqda")
        vaqt.write_text(json.dumps({"sinf": sinf, "kitob": pdf.stem, "mavzu": m["mavzu"],
                                    "savollar": savollar}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        txt_yoz(jf.with_suffix(".txt"), m["mavzu"], savollar)
        vaqt.replace(jf)
        yoz(f"    [{k}/{len(mavzular)}] {m['mavzu']} - {len(savollar)} ta")

    ish = list(enumerate(mavzular, 1))
    if PARALLEL > 1:
        with ThreadPoolExecutor(max_workers=PARALLEL) as ex:
            natijalar = [ex.submit(bitta_mavzu, k, m) for k, m in ish]
            limit = None
            for f in natijalar:
                try:
                    f.result()
                except LimitTugadi as e:
                    limit = e
        if limit:
            raise limit
    else:
        for k, m in ish:
            bitta_mavzu(k, m)

    # hamma mavzu tayyor bo'lsa - bitta umumiy fayl
    tayyor = [papka / (fayl_nomi(k, m["mavzu"]) + ".json") for k, m in enumerate(mavzular, 1)]
    tayyor = [f for f in tayyor if f.exists()]
    birlashgan = [json.loads(f.read_text(encoding="utf-8")) for f in tayyor]
    (papka / "_TOLIQ.json").write_text(json.dumps(birlashgan, ensure_ascii=False, indent=1),
                                       encoding="utf-8")


def tartib(p):
    # 3-sinf, 4-sinf ... 11-sinf to'g'ri tartibda bo'lishi uchun
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", str(p))]


def holat(pdflar):
    jami_t = jami_m = 0
    for pdf in pdflar:
        papka = natija_papkasi(pdf)
        mf = papka / "_mavzular.json"
        nom = pdf.relative_to(KITOBLAR_PAPKASI)
        if not mf.exists():
            print(f"  [ ] {nom} - boshlanmagan")
            continue
        m = len(json.loads(mf.read_text(encoding="utf-8")))
        t = len([f for f in papka.glob("[0-9]*.json")])
        jami_t, jami_m = jami_t + t, jami_m + m
        belgi = "[x]" if t >= m else "[~]"
        print(f"  {belgi} {nom} - {t}/{m} mavzu")
    print(f"\nJami: {len(pdflar)} kitob, boshlanganlarida {jami_t}/{jami_m} mavzu tayyor")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pdflar = sorted(KITOBLAR_PAPKASI.rglob("*.pdf"), key=tartib)
    if args:
        pdflar = [p for p in pdflar
                  if any(a.lower() in str(p.relative_to(KITOBLAR_PAPKASI)).lower() for a in args)]
    if "--holat" in sys.argv:
        holat(pdflar)
        return

    print(f"{len(pdflar)} ta PDF topildi\n")
    for n, pdf in enumerate(pdflar, 1):
        print(f"[{n}/{len(pdflar)}] {pdf.relative_to(KITOBLAR_PAPKASI)}")
        try:
            kitob(pdf)
        except LimitTugadi as e:
            print("\nLimit tugadi. Keyinroq qayta ishga tushiring - ish shu joydan davom etadi.")
            print(e)
            return
        except Exception as e:
            print(f"  ! xato: {e}")
    print("\nHammasi tayyor!")


if __name__ == "__main__":
    main()
