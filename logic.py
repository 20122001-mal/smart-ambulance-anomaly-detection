import numpy as np

def compute_risk(vitals):
    hr = vitals["heart_rate"]
    spo2 = vitals["spo2"]
    bp = vitals["systolic_bp"]

    hr_risk = np.clip((hr - 90) / 40, 0, 1)
    spo2_risk = np.clip((95 - spo2) / 10, 0, 1)
    bp_risk = np.clip((110 - bp) / 40, 0, 1)

    risk_score = (0.4 * hr_risk + 0.4 * spo2_risk + 0.2 * bp_risk) * 100

    anomaly = risk_score > 40
    confidence = min(1.0, risk_score / 100)
    alert = (risk_score > 60) and (confidence > 0.6)

    return {
        "anomaly": anomaly,
        "risk_score": round(risk_score, 2),
        "confidence": round(confidence, 2),
        "alert": alert
    }
