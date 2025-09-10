@echo off
REM JICC Windows 啟動腳本
REM 類似 Odoo 的 odoo-bin

echo 啟動 JICC 系統...
echo.

REM 檢查虛擬環境
if not exist ".venv_py31\Scripts\python.exe" (
    echo 錯誤: 找不到虛擬環境 .venv_py31
    echo 請先創建虛擬環境
    pause
    exit /b 1
)

REM 使用虛擬環境的 Python 運行主腳本
.venv_py31\Scripts\python.exe jicc-bin

pause
