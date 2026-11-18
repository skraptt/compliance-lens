#!/usr/bin/env bash
# Start the local Compliance Lens server for the Word add-in. Keep this window open.
#   ./scripts/start.sh            picks Claude Code (your Claude plan) if logged in, else the API key
#   ./scripts/start.sh --backend api
set -euo pipefail
cd "$(dirname "$0")/.."

claude_logged_in() {
  command -v claude >/dev/null && .venv/bin/python -c 'import sys; from lens.claude_cli import auth_status; sys.exit(0 if auth_status().get("loggedIn") else 1)' 2>/dev/null
}
[ -x .venv/bin/python ] || { echo "Run ./scripts/setup.sh first."; exit 1; }

args=("$@")
if [[ " $* " != *" --backend "* ]]; then
  if claude_logged_in; then
    args+=(--backend claude-code)
  elif [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo "No Claude access: run 'claude auth login' (Claude Code) or export ANTHROPIC_API_KEY."; exit 1
  fi
fi
exec .venv/bin/python -m lens serve "${args[@]}"
