#!/bin/bash
# Mac uchun: shu faylni ikki marta bosing.
# Faqat bitta sinf kerak bo'lsa terminalda: ./ishga_tushir.command 7-sinf
cd "$(dirname "$0")" || exit 1
export PYTHONUTF8=1

PY=$(command -v python3 || command -v python)
if [ -z "$PY" ]; then
  echo "Python topilmadi. https://www.python.org saytidan o'rnating."
  read -r -p "Yopish uchun Enter bosing..." _
  exit 1
fi

[ -d ".claude" ] || cp -R "_claude" ".claude"

echo "Kutubxonalar tekshirilmoqda..."
"$PY" -m pip install -q -r requirements.txt

echo
"$PY" test_generator.py "$@"
echo
read -r -p "Yopish uchun Enter bosing..." _
