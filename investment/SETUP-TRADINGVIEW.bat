@echo off
setlocal EnableExtensions
title TradingView MCP Setup for Cursor
echo.
echo Setup runs from the Consultant-agents repo root, not this investment\ folder.
echo.

cd /d "%~dp0.."
if not exist "SETUP-TRADINGVIEW.bat" (
  echo ERROR: expected parent folder to be Consultant-agents\ with SETUP-TRADINGVIEW.bat.
  echo Open Consultant-agents\ in Cursor, not only investment\.
  pause
  exit /b 1
)

call "%CD%\SETUP-TRADINGVIEW.bat"
