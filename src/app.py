from flask import Flask,request,jsonify
import os
import joblib
import logging
import numpy as np


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(
    BASE_DIR,
    "model",
    "linear_regression_model.pkl"
)

scaler_path = os.path.join(
    BASE_DIR,
    "model",
    "scaler.pkl"
)

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route("/predict",methods =['POST'])
def predict_performance_student():
    payload = request.get_json()

    try:
        data = [
            float(payload.get("hour_studies")),
            float(payload.get("previous_scores")),
            int(payload.get("extracurricular_activities")),
            float(payload.get("sleep_hours")),
            int(payload.get("sample_question"))
        ]
        
        X =  np.array(data).reshape(1,-1)
        X_scaled = scaler.transform(X)
        
        result = model.predict(X_scaled)
        app.logger.info(f"Prediction result: {result}")

        return jsonify({
            "prediction": float(result[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400