#!/usr/bin/env bash
set -euo pipefail

# Simple helper to create venv, install deps and run the Flask form locally.
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -m venv "$ROOT_DIR/venv"
source "$ROOT_DIR/venv/bin/activate"
pip install -r "$ROOT_DIR/requirements.txt"

# Optional: export these to change host/port/debug
export FLASK_HOST=${FLASK_HOST:-0.0.0.0}
export FLASK_PORT=${FLASK_PORT:-5000}
export FLASK_DEBUG=${FLASK_DEBUG:-True}

python "$ROOT_DIR/app.py"
