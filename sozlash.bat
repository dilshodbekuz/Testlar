@echo off
cd /d "%~dp0"
if not exist ".claude" xcopy /E /I /Y "_claude" ".claude" >nul
echo Claude Code sozlamalari tayyor (.claude papkasi).
pause
