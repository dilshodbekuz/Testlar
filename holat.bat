@echo off
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0"

set PY=
python --version >nul 2>&1 && set PY=python
if not defined PY py -3 --version >nul 2>&1 && set PY=py -3
if not defined PY (
  echo Python topilmadi. https://www.python.org saytidan o'rnating.
  pause
  exit /b 1
)

%PY% test_generator.py --holat
pause
