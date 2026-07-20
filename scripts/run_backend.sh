#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
source "$ROOT/.venv/bin/activate"
export PYTHONPATH="$ROOT/core:$ROOT/backend:${PYTHONPATH:-}"
cd "$ROOT/backend"
exec uvicorn app:app --host 0.0.0.0 --port 8000 --reload
