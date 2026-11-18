#!/usr/bin/env bash
# One-time set-up for Compliance Lens on macOS or Linux.
#   ./scripts/setup.sh
# Creates .venv with the Python packages, installs a trusted HTTPS certificate for
# localhost (Word only loads add-ins over HTTPS) and, on a Mac with Word, sideloads the add-in.
set -euo pipefail
cd "$(dirname "$0")/.."

claude_logged_in() {
  command -v claude >/dev/null && .venv/bin/python -c 'import sys; from lens.claude_cli import auth_status; sys.exit(0 if auth_status().get("loggedIn") else 1)' 2>/dev/null
}

ok()   { printf '  \033[32m✓\033[0m %s\n' "$1"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✗\033[0m %s\n' "$1"; exit 1; }

echo "Compliance Lens set-up"

# 1. Python 3.10+ and packages in a local virtual environment
command -v python3 >/dev/null || fail "Python 3 not found. Install it from https://www.python.org/downloads/"
python3 -c 'import sys; sys.exit(sys.version_info < (3, 10))' || fail "Python 3.10 or newer is needed (found $(python3 -V))."
[ -d .venv ] || python3 -m venv --system-site-packages .venv
.venv/bin/python -m pip install --quiet -r requirements.txt
ok "Python packages installed in .venv"

# 2. HTTPS certificate for localhost
if [ -f "$HOME/.office-addin-dev-certs/localhost.crt" ]; then
  ok "Certificate for https://localhost already installed"
elif command -v npx >/dev/null; then
  echo "  Installing a certificate for https://localhost (your password may be asked to trust it)…"
  npx --yes office-addin-dev-certs install >/dev/null
  ok "Certificate installed in ~/.office-addin-dev-certs"
else
  fail "Node.js not found; it is needed once to create the certificate. Install it from https://nodejs.org and run this script again."
fi

# 3. Sideload into Word for Mac, if installed
WEF="$HOME/Library/Containers/com.microsoft.Word/Data/Documents/wef"
if [ "$(uname)" = "Darwin" ] && [ -d "$HOME/Library/Containers/com.microsoft.Word" ]; then
  mkdir -p "$WEF" && cp addin/manifest.xml "$WEF/"
  ok "Add-in registered with Word for Mac (restart Word to see it)"
else
  warn "Word desktop for Mac not found. Use Word on the web: Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in → addin/manifest.xml"
fi

# 4. A way to reach Claude
if claude_logged_in; then
  ok "Claude Code is logged in: scans will use your Claude subscription"
elif [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  ok "ANTHROPIC_API_KEY is set: scans will use the API"
else
  warn "No Claude access yet. Either install Claude Code and run 'claude auth login' (uses your Claude plan), or export ANTHROPIC_API_KEY."
fi

echo
echo "Done. Start the server with:  ./scripts/start.sh"
