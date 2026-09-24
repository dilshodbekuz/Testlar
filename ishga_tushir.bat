@echo off
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0"

set PY=
python --version >nul 2>&1 && set PY=python
if not defined PY py -3 --version >nul 2>&1 && set PY=py -3
if not defined PY (
  echo Python topilmadi. https://www.python.org saytidan o'rnating
  echo ^(o'rnatishda "Add Python to PATH" katagini belgilang^).
  pause
  exit /b 1
)

if not exist ".claude" xcopy /E /I /Y "_claude" ".claude" >nul
echo Kutubxonalar tekshirilmoqda...
%PY% -m pip install -q -r requirements.txt
echo.
%PY% test_generator.py %*
echo.
pause
