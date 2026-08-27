@echo off
setlocal EnableExtensions
title IB TWS Bond Screening Setup for Grot Bot
echo.
echo ============================================
echo  IB TWS Bond Screening - Setup helper
echo ============================================
echo.

cd /d "%~dp0.."
echo Working folder: %CD%
echo.

echo [1/3] Installing Python packages (ib_insync, pyyaml, yfinance)...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r investment\scripts\requirements-tradingview.txt
if errorlevel 1 py -m pip install -r investment\scripts\requirements-tradingview.txt

echo.
echo [2/3] Checking for TWS / IB Gateway on localhost...
powershell -NoProfile -Command "try { $c = New-Object Net.Sockets.TcpClient; $c.Connect('127.0.0.1',7497); $c.Close(); Write-Host '  Port 7497 (paper) is OPEN - TWS/Gateway likely running.' } catch { Write-Host '  Port 7497 (paper) is CLOSED - start TWS or IB Gateway first.' }"
powershell -NoProfile -Command "try { $c = New-Object Net.Sockets.TcpClient; $c.Connect('127.0.0.1',7496); $c.Close(); Write-Host '  Port 7496 (live) is OPEN.' } catch { Write-Host '  Port 7496 (live) is CLOSED.' }"

echo.
echo [3/3] Next steps (manual in TWS):
echo   1. File -^> Global Configuration -^> API -^> Settings
echo   2. Enable ActiveX and Socket Clients
echo   3. Socket port: 7497 (paper) or 7496 (live)
echo   4. Trusted IP: 127.0.0.1
echo   5. Restart TWS, then test:
echo      python investment\scripts\bond_screen_ib.py --preset corp-us
echo.
echo Full guide: investment\SETUP-IB-TWS.md
echo.
pause
