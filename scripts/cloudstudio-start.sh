#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python is required but was not found."
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "Node.js and npm are required but were not found."
  exit 1
fi

if [[ ! -f "$BACKEND_DIR/law_game.db" ]]; then
  cp "$ROOT_DIR/database/law_game.db" "$BACKEND_DIR/law_game.db"
fi

if [[ ! -f "$BACKEND_DIR/.env" ]]; then
  cp "$BACKEND_DIR/.env.example" "$BACKEND_DIR/.env"
fi

if [[ ! -d "$BACKEND_DIR/.venv" ]]; then
  "$PYTHON_BIN" -m venv "$BACKEND_DIR/.venv"
fi

source "$BACKEND_DIR/.venv/bin/activate"
python -m pip install --disable-pip-version-check -r "$BACKEND_DIR/requirements.txt"

if [[ ! -d "$FRONTEND_DIR/node_modules" ]]; then
  npm --prefix "$FRONTEND_DIR" ci
fi

cleanup() {
  if [[ -n "${BACKEND_PID:-}" ]]; then
    kill "$BACKEND_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM

export DEBUG=false

(
  cd "$BACKEND_DIR"
  python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
) &
BACKEND_PID=$!

for attempt in {1..30}; do
  if curl --fail --silent http://127.0.0.1:8000/health >/dev/null; then
    break
  fi
  if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
    echo "Backend failed to start."
    exit 1
  fi
  sleep 1
done

if ! curl --fail --silent http://127.0.0.1:8000/health >/dev/null; then
  echo "Backend health check timed out."
  exit 1
fi

echo "Backend: http://127.0.0.1:8000"
echo "Frontend: open the Cloud Studio preview for port 5173"
npm --prefix "$FRONTEND_DIR" run dev -- --host 0.0.0.0 --port 5173
