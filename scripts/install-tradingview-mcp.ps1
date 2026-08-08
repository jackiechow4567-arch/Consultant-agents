# Install TradingView MCP dependencies (Windows)
# Run in PowerShell: .\scripts\install-tradingview-mcp.ps1

Write-Host "Installing uv (if missing)..."
if (-not (Get-Command uvx -ErrorAction SilentlyContinue)) {
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  $env:PATH = "$env:USERPROFILE\.local\bin;$env:LOCALAPPDATA\Programs\uv;$env:PATH"
}

Write-Host "Installing tradingview-assistant + compatible MCP..."
pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2"

Write-Host "Smoke test..."
uvx --from tradingview-assistant --with "mcp[cli]>=1.12.0,<2" tradingview-mcp --help
if ($LASTEXITCODE -ne 0) {
  Write-Error "TradingView MCP failed to start. Copy the error above."
  exit 1
}

Write-Host "OK. Restart Cursor fully, then check Settings -> Tools & MCP -> tradingview (green dot)."
