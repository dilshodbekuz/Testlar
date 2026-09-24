#!/bin/bash
# Mac uchun: qaysi kitob qancha tayyor ekanini ko'rsatadi.
cd "$(dirname "$0")" || exit 1
export PYTHONUTF8=1

PY=$(command -v python3 || command -v python)
if [ -z "$PY" ]; then
  echo "Python topilmadi. https://www.python.org saytidan o'rnating."
  read -r -p "Yopish uchun Enter bosing..." _
  exit 1
fi

"$PY" test_generator.py --holat
echo
read -r -p "Yopish uchun Enter bosing..." _
