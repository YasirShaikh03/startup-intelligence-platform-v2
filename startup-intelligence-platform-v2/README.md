# 🚀 Startup Intelligence Platform — Pro Edition v2

A production-grade, AI-powered business scoring and analysis platform for **startups** and **street businesses**. Built as a final-year top project with real-world architecture.

---

## ✨ What's New in v2

| Feature | v1 (Original) | v2 (This Release) |
|---|---|---|
| AI Engine | Claude API only | **FastAPI → Claude API → Offline** cascade |
| Backend | None | **FastAPI + Python ML engine** |
| Theme | Dark only | **Light + Dark mode toggle** |
| Export | JSON + Print | **JSON Report + PDF + Share + Print** |
| Backend Status | Not shown | **Live connection indicator** |
| Code structure | Single file | **Modular frontend + backend/** |
| API Endpoints | None | `/predict` `/analyze` `/compare` `/growth` |

---

## 📁 Folder Structure

```
startup-intelligence-platform/
├── frontend/
│   ├── index.html        ← Main UI (HTML5)
│   ├── style.css         ← Dark + Light theme (CSS variables)
│   ├── script.js         ← Logic, scoring engine, charts, API calls
│   └── chart.min.js      ← Chart.js local fallback (offline use)
│
├── backend/
│   ├── main.py           ← FastAPI app + all route handlers
│   ├── model.py          ← ML scoring engine + AI insights generator
│   └── requirements.txt  ← Python dependencies
│
├── setup.sh              ← One-command setup script
└── README.md             ← This file
```

---

## 🔧 Setup & Run

### Prerequisites
- Python 3.9+
- A modern browser (Chrome, Firefox, Edge)
- Optional: Node.js (for `npx serve` alternative to Python http.server)

### Step 1 — Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate       # Mac/Linux
# .venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn main:app --reload --port 8000
```

The FastAPI server starts at `http://localhost:8000`
- Interactive API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Step 2 — Frontend

```bash
cd frontend

# Option A: Python built-in server
python3 -m http.server 5500

# Option B: Node.js
npx serve . -p 5500

# Option C: VS Code Live Server
# Right-click index.html → "Open with Live Server"
```

Open `http://localhost:5500` in your browser.

### One-Command Setup (Mac/Linux)
```bash
chmod +x setup.sh && ./setup.sh
```

---

## 🧠 Architecture Deep-Dive

### AI Cascade (3-tier fallback)
```
User submits form
      │
      ▼
[1] FastAPI /analyze ──→ Python ML engine + AI insights
      │ (if offline/error)
      ▼
[2] Claude API (claude-sonnet-4-20250514) ──→ JSON insights
      │ (if API key missing/error)
      ▼
[3] Offline JS Engine ──→ Rule-based consulting output
      │
      ▼
Result rendered — ALWAYS WORKS
```

### Scoring Engine (8 Dimensions — Startup)
| Dimension | Weight | What It Measures |
|---|---|---|
| Traction | 24% | Revenue, product stage, growth rate |
| Market | 20% | TAM, competition, trend, seasonality |
| Team | 18% | Founder experience × team size |
| Funding | 14% | Stage + amount invested |
| Moat | 10% | Defensibility of position |
| Operations | 6% | Legal, employees, breakeven |
| Digital | 4% | Online presence, aggregators |
| Timing | 4% | Industry timing score |

### Scoring Engine (6 Dimensions — Street Food)
| Dimension | Weight | What It Measures |
|---|---|---|
| Location | 28% | Footfall, landmarks, competition, weather |
| Product | 25% | Food demand × hygiene × taste × waste |
| Finance | 22% | Margin, breakeven, revenue, seasonality |
| Ops / Legal | 12% | License, police risk, waste management |
| Digital / Growth | 8% | Online presence, aggregators, growth rate |
| Survival Buffer | 5% | Combined resilience score |

### Backend API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Server health check |
| GET | `/benchmarks` | Category benchmark data |
| POST | `/predict` | Score prediction only |
| POST | `/analyze` | Full analysis + AI insights |
| POST | `/compare` | Side-by-side comparison |
| POST | `/growth` | Revenue projection |

---

## 🎯 Features at a Glance

### Core Analysis
- 🧠 **ML Scoring Engine** — 8-dimension weighted model with adaptive adjustments
- 🤖 **AI Deep Analysis** — Strengths, risks, opportunities, actions, scaling strategy
- 📊 **4 Charts** — Radar, Bar, Line, Doughnut with gradient animations
- 📈 **18-Month Revenue Forecast** — Interactive with 3 scenarios + seasonality

### Advanced Tools
- ⚖️ **Business Comparison** — Side-by-side radar chart + winner analysis
- 🔮 **What-If Scenarios** — Simulate pricing, hiring, expansion decisions
- 💬 **AI Chat Q&A** — Multi-turn business consultant chat
- ⚖️ **Break-Even Calculator** — Visual cost vs revenue chart
- 💼 **Funding Readiness Meter** — VC-criteria scoring
- 🇮🇳 **Government Scheme Matcher** — MUDRA, Startup India, etc.
- 📅 **Monthly Score Tracker** — Progress over time
- 🚀 **Pitch Deck Generator** — 10-slide deck with Claude AI
- 📝 **Business Plan Writer** — 5-section plan with AI

### UX
- 🌓 **Light / Dark mode toggle** — Persistent across sessions
- 🟢 **Backend status indicator** — Live connection badge
- 📋 **Analysis history** — LocalStorage with export
- 🔗 **Shareable report links** — URL-encoded hash
- ⬇️ **JSON + PDF export** — Formatted reports

---

## 🛠 Tech Stack

### Frontend
- Vanilla JavaScript (ES2022, no framework needed)
- Chart.js 4.4 (CDN + local fallback)
- CSS Custom Properties (light/dark themes)
- LocalStorage for history, theme, and tracker

### Backend
- **FastAPI** (Python 3.9+)
- **Pydantic v2** for request validation
- Pure Python ML scoring engine (no scikit-learn needed)
- CORS enabled for localhost development

### AI
- **Claude claude-sonnet-4-20250514** via Anthropic API (optional)
- **FastAPI backend** ML insights (no API key needed)
- **Offline engine** (always available, no internet required)

---

## 🎓 Final Year Project Notes

This project demonstrates:
1. **Full-stack architecture** — Decoupled frontend + REST API backend
2. **Graceful degradation** — 3-tier AI fallback ensures 100% uptime
3. **Production patterns** — CORS, health checks, request validation, error handling
4. **Business logic** — Real ML scoring engine derived from industry data
5. **UX engineering** — Theme system, loading states, responsive design
6. **Data modeling** — Pydantic schemas, structured JSON APIs

---

## 📄 License

MIT License — Free to use, modify, and present as your project.

---

*Built with ❤️ — Startup Intelligence Platform Pro v2*
