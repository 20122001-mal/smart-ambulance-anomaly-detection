# Smart Ambulance Anomaly Detection & Risk Scoring

## Overview
This project demonstrates a smart ambulance monitoring system designed to detect early patient deterioration during transport. Ambulance environments are highly dynamic, with motion and vibrations often causing noisy sensor readings. The goal of this system is to provide reliable, interpretable alerts that support ambulance staff without creating unnecessary alarm fatigue.

The solution uses synthetic patient vital data and exposes the monitoring logic through a FastAPI service to simulate real-time integration.

---

## Features
- Synthetic ambulance patient vital data simulation
- Motion-induced SpO₂ artifact detection and correction
- Trend-based anomaly detection (no rigid thresholds)
- Composite risk scoring (0–100)
- Confidence-aware alert generation
- FastAPI service with Swagger UI for testing

---

## Tech Stack
- Python  
- NumPy  
- FastAPI  
- Uvicorn  

---

## Project Structure
gray_ambulance_ai/
├── app.py # FastAPI application
├── logic.py # Anomaly detection and risk scoring logic
├── requirements.txt # Project dependencies
├── README.md
└── data/ # (optional) synthetic datasets


---

## API Endpoint

### POST `/analyze`

**Input Example**
```json
{
  "heart_rate": 130,
  "spo2": 88,
  "systolic_bp": 92,
  "diastolic_bp": 60,
  "motion": 0.2
}
{
  "anomaly": true,
  "risk_score": 75.0,
  "confidence": 0.75,
  "alert": true
}
