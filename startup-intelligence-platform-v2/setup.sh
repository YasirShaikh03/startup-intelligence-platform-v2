#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
#  Startup Intelligence Platform v2 — Setup Script
#  Run this once to set up the backend environment.
# ═══════════════════════════════════════════════════════════════════

set -e
cd "$(dirname "$0")"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   STARTUP INTELLIGENCE PLATFORM — Pro Edition v2            ║"
echo "║   Setup Script                                               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# ── Python backend setup ──────────────────────────────────────────
echo "▶ Setting up Python backend..."
cd backend

if ! command -v python3 &>/dev/null; then
  echo "ERROR: Python 3.9+ is required. Install from https://python.org"
  exit 1
fi

PYTHON=$(command -v python3)
echo "  Python: $($PYTHON --version)"

if [ ! -d ".venv" ]; then
  echo "  Creating virtual environment..."
  $PYTHON -m venv .venv
fi

source .venv/bin/activate
echo "  Installing dependencies..."
pip install -r requirements.txt -q

echo "  ✅ Backend ready."
cd ..

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   SETUP COMPLETE                                             ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "  HOW TO RUN:"
echo ""
echo "  Terminal 1 — Start backend:"
echo "    cd backend && source .venv/bin/activate"
echo "    uvicorn main:app --reload --port 8000"
echo ""
echo "  Terminal 2 — Serve frontend:"
echo "    cd frontend && python3 -m http.server 5500"
echo ""
echo "  Then open: http://localhost:5500"
echo ""
echo "  Backend API docs: http://localhost:8000/docs"
echo "  Backend health:   http://localhost:8000/health"
echo ""
