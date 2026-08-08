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

REM --- 1. Install uv (provides uvx) ---
where uvx >nul 2>&1
if errorlevel 1 (
  echo [1/4] Installing uv...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
) else (
  echo [1/4] uvx already installed.
)

set "UVPATH=%USERPROFILE%\.local\bin;%LOCALAPPDATA%\Programs\uv"
set "PATH=%UVPATH%;%PATH%"

REM --- 2. Python packages (fallback) ---
echo [2/4] Installing Python packages...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2" "tradingview-screener" >nul 2>&1
if errorlevel 1 (
  py -m pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2" "tradingview-screener"
)

REM --- 3. Write Cursor MCP config ---
echo [3/4] Writing .cursor\mcp.json ...
if not exist ".cursor" mkdir ".cursor"
(
echo {
echo   "mcpServers": {
echo     "tradingview": {
echo       "command": "uvx",
echo       "args": [
echo         "--from",
echo         "tradingview-assistant",
echo         "--with",
echo         "mcp[cli]^^>=1.12.0,^^<2",
echo         "tradingview-mcp"
echo       ],
echo       "env": {
echo         "PATH": "${env:USERPROFILE}\\.local\\bin;${env:LOCALAPPDATA}\\Programs\\uv;${env:PATH}"
echo       }
echo     }
echo   }
echo }
) > ".cursor\mcp.json"

REM --- 4. Smoke test ---
echo [4/4] Testing TradingView MCP...
uvx --from tradingview-assistant --with "mcp[cli]>=1.12.0,<2" tradingview-mcp --help >nul 2>&1
if errorlevel 1 (
  echo.
  echo WARNING: uvx test failed. Trying Python fallback config...
  (
  echo {
  echo   "mcpServers": {
  echo     "tradingview": {
  echo       "command": "python",
  echo       "args": ["-m", "tradingview_mcp.server", "stdio"]
  echo     }
  echo   }
  echo }
  ) > ".cursor\mcp.json"
  python -m tradingview_mcp.server --help >nul 2>&1
  if errorlevel 1 py -m tradingview_mcp.server --help >nul 2>&1
)

echo.
echo ============================================
echo  DONE - 3 steps left for YOU:
echo ============================================
echo  1. Open Cursor
echo  2. File -^> Open Folder -^> select THIS folder:
echo     %CD%
echo  3. Fully quit Cursor, reopen, then check:
echo     Settings -^> Tools ^& MCP -^> tradingview = GREEN
echo.
echo  Test in chat (Ctrl+L):
echo  "Using TradingView MCP, show top US stock gainers"
echo.
pause
