@echo off
REM JICC Windows �Ұʸ}��
REM ���� Odoo �� odoo-bin

echo �Ұ� JICC �t��...
echo.

REM �ˬd��������
if not exist ".venv_py31\Scripts\python.exe" (
    echo ���~: �䤣��������� .venv_py31
    echo �Х��Ыص�������
    pause
    exit /b 1
)

REM �ϥε������Ҫ� Python �B��D�}��
.venv_py31\Scripts\python.exe jicc-bin

pause
