#!/usr/bin/env bash
set -euo pipefail

if ! command -v uvx >/dev/null 2>&1; then
  echo "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

echo "Installing tradingview-assistant + compatible MCP..."
pip install "tradingview-assistant" "mcp[cli]>=1.12.0,<2"

echo "Smoke test..."
uvx --from tradingview-assistant --with "mcp[cli]>=1.12.0,<2" tradingview-mcp --help

echo "OK. Open Consultant-agents/ in Cursor (File -> Open Folder), not only investment/."
echo "Restart Cursor fully, then check Settings -> Tools & MCP -> tradingview (green dot)."
