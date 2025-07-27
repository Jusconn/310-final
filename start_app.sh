#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -q -r requirements.txt

echo "Starting API on http://localhost:5001"
python src/api/api.py & python gui/main.py