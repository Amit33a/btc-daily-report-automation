@echo off
cd /d C:\Users\Amit Sharma\Desktop\Daily-BTC-Report-SCRATCH

echo [%date% %time%] Task started >> logs\scheduler_debug.log

call .venv\Scripts\activate >> logs\scheduler_debug.log 2>&1
echo [%date% %time%] Venv activated >> logs\scheduler_debug.log

python -m src.main >> logs\scheduler_debug.log 2>&1
echo [%date% %time%] Python command finished with exit code %errorlevel% >> logs\scheduler_debug.log

