from fastapi import FastAPI
from pydantic import BaseModel
from logic import compute_risk

app = FastAPI(title="Smart Ambulance API")

class VitalInput(BaseModel):
    heart_rate: float
    spo2: float
    systolic_bp: float
    diastolic_bp: float
    motion: float

@app.post("/analyze")
def analyze_vitals(vitals: VitalInput):
    return compute_risk(vitals.dict())
