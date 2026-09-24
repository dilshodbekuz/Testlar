@echo off
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0"
if not exist ".claude" xcopy /E /I /Y "_claude" ".claude" >nul
echo Kutubxonalar tekshirilmoqda...
python -m pip install -q -r requirements.txt
echo.
python test_generator.py %*
echo.
pause
