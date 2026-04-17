## Author

Yasir Shaikh

GitHub: https://github.com/YasirShaikh03

# 🚀 Startup Intelligence Platform — Pro Edition v2

An ML-powered business analysis system that evaluates startups and street businesses using real-world signals, scoring models, and AI-driven insights.

---

## 🔍 Overview

This platform analyzes a business based on multiple parameters like market, revenue, team, location, and operations.

It generates:

* A **composite score (0–100)**
* Category-wise performance (Survival, Profitability, Scalability, Dominance)
* A **verdict** (STRONG PASS / CONDITIONAL PASS / WATCH / HARD PASS)
* AI-powered insights and recommendations
* Growth predictions and scenario simulations

---

## ⚙️ Core Features

### 📊 Scoring Engine

* Multi-factor weighted scoring system
* Separate models for:

  * Startups
  * Street businesses
* ML-style adjustment layer based on combined signals

---

### 🤖 AI Analysis

* AI-generated business insights
* Offline fallback if API is unavailable
* Context-aware recommendations

---

### 📈 Prediction & Simulation

* Revenue forecasting (base / bull / bear scenarios)
* Break-even analysis
* Growth modeling

---

### 🧩 Advanced Capabilities

* Industry benchmark comparison
* Multi-business comparison
* What-if scenario simulation
* JSON export and local history tracking

---

## 🏗️ Architecture

```id="a1k3n9"
Frontend (HTML, CSS, JS)
        ↓
FastAPI Backend (API + Logic)
        ↓
ML Scoring Engine
        ↓
AI Insight Layer (Claude / Offline)
```

---

## 🖥️ Tech Stack

### Backend

* FastAPI
* Python
* Pydantic
* Uvicorn

### Frontend

* Vanilla JavaScript
* Chart.js
* HTML + CSS

---

## 🚀 Setup Instructions

### 1. Clone repository

```bash id="b2m7qp"
git clone https://github.com/your-username/startup-intelligence-platform.git
cd startup-intelligence-platform
```

---

### 2. Run setup

```bash id="c9x4zs"
bash setup.sh
```

---

### 3. Start backend

```bash id="d4t8vn"
cd backend
source .venv/bin/activate
uvicorn main:app --reload --port 8000
```

---

### 4. Start frontend

```bash id="e7p1lk"
cd frontend
python3 -m http.server 5500
```

---

### 5. Open in browser

```id="f6q2mw"
http://localhost:5500
```

API Docs:

```id="g5r9yx"
http://localhost:8000/docs
```

---

## 📊 Scoring Model

### Startup Model

* Traction (24%)
* Market (20%)
* Team (18%)
* Funding (14%)
* Moat + Operations + Digital + Timing

### Street Business Model

* Location (28%)
* Product (25%)
* Finance (22%)
* Operations (15%)
* Growth (10%)

Final score = weighted base + adaptive adjustment

---

## ⚠️ Limitations

* Heuristic-based ML (not trained on real datasets)
* AI output depends on API availability
* Not production deployed

---

## 👤 Author

## Author

Yasir Shaikh

GitHub: https://github.com/YasirShaikh03

---

## 📜 License

MIT License
