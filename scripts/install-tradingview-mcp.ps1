# Install TradingView MCP dependencies (Windows)
# Run from Consultant-agents repo root: .\scripts\install-tradingview-mcp.ps1
# Do not open only investment\ in Cursor — skills load from the repo root.

$repoRoot = $PSScriptRoot
if ((Split-Path $repoRoot -Leaf) -eq "scripts") {
  $repoRoot = Split-Path $repoRoot -Parent
}
if ((Split-Path $repoRoot -Leaf) -eq "investment") {
  $repoRoot = Split-Path $repoRoot -Parent
}
if (-not (Test-Path (Join-Path $repoRoot ".cursor\skills"))) {
  Write-Error "Open Consultant-agents\ (repo root) in Cursor, not only investment\."
  exit 1
}
Set-Location $repoRoot
Write-Host "Repo root: $repoRoot"

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

$cursorDir = Join-Path (Get-Location) ".cursor"
if (-not (Test-Path $cursorDir)) { New-Item -ItemType Directory -Path $cursorDir | Out-Null }
Copy-Item -Force (Join-Path (Get-Location) ".cursor/mcp.windows.json") (Join-Path $cursorDir "mcp.json")
Write-Host "Wrote .cursor/mcp.json"

Write-Host "OK. In Cursor: File -> Open Folder -> Consultant-agents (repo root), not investment\."
Write-Host "Restart Cursor fully, then check Settings -> Tools & MCP -> tradingview (green dot)."
