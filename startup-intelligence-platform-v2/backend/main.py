from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import datetime
import uuid

from model import (
    compute_startup_score,
    compute_street_score,
    generate_ai_insights,
    compare_businesses,
    get_benchmarks,
    predict_growth,
)

app = FastAPI(
    title="Startup Intelligence Platform API",
    description="ML-powered business scoring, analysis, and prediction engine.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BusinessInput(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    biz_type: Optional[str] = ""
    industry: Optional[str] = ""
    city: Optional[str] = ""
    state: Optional[str] = ""
    area: Optional[str] = ""
    description: Optional[str] = ""
    is_street: bool = False

    food_type: Optional[str] = ""
    stall_type: Optional[str] = ""
    daily_cust: Optional[float] = 0
    avg_price: Optional[float] = 0
    peak_hrs: Optional[str] = ""
    hygiene: Optional[str] = ""
    repeat_rate: Optional[float] = 0
    taste_rating: Optional[float] = 0
    daily_waste: Optional[float] = 0
    rm_var: Optional[str] = ""
    footfall: Optional[str] = ""
    landmarks: Optional[str] = ""
    dist_sta: Optional[str] = ""
    dist_col: Optional[str] = ""
    area_comp: Optional[str] = ""
    crowd_type: Optional[str] = ""

    fexp: Optional[str] = ""
    tsize: Optional[str] = ""
    rev: Optional[str] = ""
    pstage: Optional[str] = ""
    fstage: Optional[str] = ""
    famt: Optional[str] = ""
    msize: Optional[str] = ""

    daily_rev: Optional[float] = 0
    monthly_rev: Optional[float] = 0
    margin: Optional[float] = 0
    growth_rate: Optional[float] = 0
    cost_unit: Optional[float] = 0
    sell_price: Optional[float] = 0
    breakeven: Optional[str] = ""
    rent: Optional[float] = 0
    ad_spend: Optional[float] = 0
    employees: Optional[int] = 0
    biz_age: Optional[str] = ""

    comp: Optional[str] = ""
    trend: Optional[str] = ""
    seasonal: Optional[str] = ""
    weather: Optional[str] = ""
    expansion: Optional[str] = ""
    diff: Optional[str] = ""

    license: Optional[str] = ""
    police: Optional[str] = ""
    online: Optional[str] = ""
    aggr: Optional[str] = ""
    marketing: Optional[str] = ""


class CompareInput(BaseModel):
    business_a: BusinessInput
    business_b: BusinessInput


class GrowthInput(BaseModel):
    base_revenue: float
    growth_rate: float
    months: int = Field(default=12, ge=1, le=36)
    scenario: str = Field(default="base", pattern="^(base|bull|bear)$")
    seasonality: float = Field(default=1.0, ge=0.5, le=1.0)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Startup Intelligence Platform API",
        "version": "2.0.0",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    }


@app.get("/benchmarks")
def benchmarks():
    return {"benchmarks": get_benchmarks()}


@app.post("/predict")
def predict(data: BusinessInput):
    try:
        is_street = data.is_street or data.biz_type == "Street Food"
        payload = data.model_dump()

        scores = compute_street_score(payload) if is_street else compute_startup_score(payload)

        score = scores["composite_score"]
        if score >= 72:
            verdict = "STRONG PASS"
        elif score >= 58:
            verdict = "CONDITIONAL PASS"
        elif score >= 42:
            verdict = "WATCH"
        else:
            verdict = "HARD PASS"

        return {
            "request_id": str(uuid.uuid4())[:8],
            "business_name": data.name,
            "is_street": is_street,
            "scores": scores,
            "verdict": verdict,
            "percentile": _score_to_percentile(score),
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze")
def analyze(data: BusinessInput):
    try:
        is_street = data.is_street or data.biz_type == "Street Food"
        payload = data.model_dump()

        scores = compute_street_score(payload) if is_street else compute_startup_score(payload)
        ai = generate_ai_insights(payload, scores, is_street)

        score = scores["composite_score"]
        if score >= 72:
            verdict = "STRONG PASS"
        elif score >= 58:
            verdict = "CONDITIONAL PASS"
        elif score >= 42:
            verdict = "WATCH"
        else:
            verdict = "HARD PASS"

        return {
            "request_id": str(uuid.uuid4())[:8],
            "business_name": data.name,
            "is_street": is_street,
            "scores": scores,
            "verdict": verdict,
            "percentile": _score_to_percentile(score),
            "insights": ai,
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/compare")
def compare(data: CompareInput):
    try:
        a_payload = data.business_a.model_dump()
        b_payload = data.business_b.model_dump()

        is_a_street = data.business_a.is_street or data.business_a.biz_type == "Street Food"
        is_b_street = data.business_b.is_street or data.business_b.biz_type == "Street Food"

        scores_a = compute_street_score(a_payload) if is_a_street else compute_startup_score(a_payload)
        scores_b = compute_street_score(b_payload) if is_b_street else compute_startup_score(b_payload)

        result = compare_businesses(
            data.business_a.name, scores_a,
            data.business_b.name, scores_b,
        )
        return {
            "request_id": str(uuid.uuid4())[:8],
            "comparison": result,
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/growth")
def growth(data: GrowthInput):
    try:
        projection = predict_growth(
            data.base_revenue,
            data.growth_rate,
            data.months,
            data.scenario,
            data.seasonality,
        )
        return {"projection": projection}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def _score_to_percentile(score: int) -> int:
    if score >= 85: return 95
    if score >= 75: return 85
    if score >= 65: return 72
    if score >= 55: return 55
    if score >= 45: return 38
    if score >= 35: return 22
    return 12
