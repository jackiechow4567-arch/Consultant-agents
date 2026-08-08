@echo off
setlocal EnableExtensions
title TradingView MCP Setup for Cursor
echo.
echo ============================================
echo  TradingView MCP - One-click setup (Windows)
echo ============================================
echo.

cd /d "%~dp0"
echo Working folder: %CD%
echo.

where uvx >nul 2>&1
if errorlevel 1 (
  echo [1/4] Installing uv...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
) else (
  echo [1/4] uvx already installed.
)

set "PATH=%USERPROFILE%\.local\bin;%LOCALAPPDATA%\Programs\uv;%PATH%"

echo [2/4] Installing Python packages...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2" "tradingview-screener" >nul 2>&1
if errorlevel 1 py -m pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2" "tradingview-screener"

echo [3/4] Writing .cursor\mcp.json ...
if not exist ".cursor" mkdir ".cursor"
copy /Y ".cursor\mcp.windows.json" ".cursor\mcp.json" >nul
if errorlevel 1 (
  echo ERROR: missing .cursor\mcp.windows.json - open this folder in Cursor from the git repo.
  pause
  exit /b 1
)

echo [4/4] Testing TradingView MCP...
uvx --from tradingview-assistant --with "mcp[cli]>=1.12.0,<2" tradingview-mcp --help >nul 2>&1
if errorlevel 1 (
  echo uvx failed - switching to Python fallback config...
  copy /Y ".cursor\mcp.python-fallback.json" ".cursor\mcp.json" >nul
)

echo.
echo ============================================
echo  DONE - finish in Cursor:
echo ============================================
echo  1. Open Cursor
echo  2. File -^> Open Folder -^> select:
echo     %CD%
echo  3. Quit Cursor completely, reopen
echo  4. Settings -^> Tools ^& MCP -^> tradingview = GREEN
echo.
echo  Test: Ctrl+L then ask for top US stock gainers
echo.
pause
