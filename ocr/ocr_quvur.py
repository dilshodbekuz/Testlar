#!/usr/bin/env python3
"""Skaner PDF -> macOS Vision OCR -> matnli PDF.

Ishlatish:  python3 ocr_quvur.py "<skaner.pdf>" "<natija.pdf>"
Har bir asl sahifa natija PDF'da ham bitta sahifa bo'lib qoladi
(mavzu sahifa oraliqlari buzilmasin).
"""
import re
import subprocess
import sys
import textwrap
from pathlib import Path

OCR = Path(__file__).parent / "ocr"
FONT, KATTALIK, QATOR_BALAND = "Helvetica", 6, 7.2
ENI, BOYI, CHET = 612, 792, 20
BELGI_QATOR = 130

ALMASH = {"ʻ": "'", "ʼ": "'", "‘": "'", "’": "'",
          "“": '"', "”": '"', "–": "-", "—": "-",
          "…": "...", " ": " ", "ё": "e", "‑": "-",
          "ı": "i", "İ": "I", "ş": "s", "Ş": "S",
          "ğ": "g", "Ğ": "G", "ə": "a", "−": "-"}


def tozala(s):
    for a, b in ALMASH.items():
        s = s.replace(a, b)
    # PDF WinAnsi'da yo'q belgilarni tashlab yuboramiz
    return "".join(c if 32 <= ord(c) < 127 or ord(c) in range(160, 256) else " "
                   for c in s)


def qalqon(s):
    return s.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def sahifa_soni(pdf):
    import pypdfium2 as pdfium
    d = pdfium.PdfDocument(str(pdf))
    n = len(d)
    d.close()
    return n


def ocr_qil(pdf, n):
    """OCR natijasini {sahifa_raqami: matn} ko'rinishida qaytaradi."""
    r = subprocess.run([str(OCR), str(pdf), "1", str(n)],
                       capture_output=True, text=True, timeout=7200)
    sahifalar, joriy = {}, None
    for qator in r.stdout.splitlines():
        m = re.match(r"^=== SAHIFA (\d+) ===$", qator)
        if m:
            joriy = int(m.group(1))
            sahifalar[joriy] = []
        elif joriy is not None:
            sahifalar[joriy].append(qator)
    return {k: "\n".join(v) for k, v in sahifalar.items()}


def pdf_yoz(sahifalar, n, yol):
    obyektlar = ["", "", "", ""]          # 1..4 band: katalog, pages, font
    sahifa_id, tarkib_id = [], []
    nav = 5
    for i in range(1, n + 1):
        matn = tozala(sahifalar.get(i, ""))
        qatorlar = []
        for xom in matn.splitlines():
            qatorlar.extend(textwrap.wrap(xom, BELGI_QATOR) or [""])
        y = BOYI - CHET
        ichi = [f"BT /F1 {KATTALIK} Tf {QATOR_BALAND} TL {CHET} {y:.1f} Td"]
        for q in qatorlar:
            ichi.append(f"({qalqon(q)}) Tj T*")
        ichi.append("ET")
        oqim = "\n".join(ichi).encode("latin-1", "replace")
        tarkib_id.append(nav)
        obyektlar.append(f"<< /Length {len(oqim)} >>\nstream\n".encode()
                         + oqim + b"\nendstream")
        nav += 1
        sahifa_id.append(nav)
        obyektlar.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {ENI} {BOYI}] "
            f"/Resources << /Font << /F1 3 0 R >> >> "
            f"/Contents {tarkib_id[-1]} 0 R >>".encode())
        nav += 1

    obyektlar[0] = b"<< /Type /Catalog /Pages 2 0 R >>"
    kids = " ".join(f"{i} 0 R" for i in sahifa_id)
    obyektlar[1] = f"<< /Type /Pages /Count {len(sahifa_id)} /Kids [{kids}] >>".encode()
    obyektlar[2] = (f"<< /Type /Font /Subtype /Type1 /BaseFont /{FONT} "
                    f"/Encoding /WinAnsiEncoding >>").encode()
    obyektlar[3] = b"<< >>"

    chiqish = bytearray(b"%PDF-1.4\n")
    siljish = []
    for i, ob in enumerate(obyektlar, start=1):
        siljish.append(len(chiqish))
        chiqish += f"{i} 0 obj\n".encode() + ob + b"\nendobj\n"
    xref = len(chiqish)
    chiqish += f"xref\n0 {len(obyektlar) + 1}\n".encode()
    chiqish += b"0000000000 65535 f \n"
    for s in siljish:
        chiqish += f"{s:010d} 00000 n \n".encode()
    chiqish += (f"trailer\n<< /Size {len(obyektlar) + 1} /Root 1 0 R >>\n"
                f"startxref\n{xref}\n%%EOF\n").encode()
    Path(yol).write_bytes(bytes(chiqish))


def main():
    manba, natija = Path(sys.argv[1]), Path(sys.argv[2])
    n = sahifa_soni(manba)
    print(f"{manba.name}: {n} sahifa, OCR boshlandi...", flush=True)
    sahifalar = ocr_qil(manba, n)
    belgi = sum(len(v) for v in sahifalar.values())
    pdf_yoz(sahifalar, n, natija)
    print(f"  tayyor: {len(sahifalar)}/{n} sahifa o'qildi, {belgi} belgi "
          f"(sahifasiga {belgi // max(1, n)}) -> {natija.name}", flush=True)


if __name__ == "__main__":
    main()
