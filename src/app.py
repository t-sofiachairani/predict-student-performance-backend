from flask import Flask,request,jsonify
import os
import joblib
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(
    BASE_DIR,
    "model",
    "LinearRegression_StudentPerformance.h5"
)
model = joblib.load(model_path)

@app.route("/predict",methods =['POST'])
def predict_performance_student():
    payload = request.get_json()

    try:
        X = [[
            float(payload.get("hour_studies")),
            float(payload.get("previous_scores")),
            int(payload.get("extracurricular_activities")),
            float(payload.get("sleep_hours")),
            int(payload.get("sample_question"))
        ]]

        result = model.predict(X)
        app.logger.info(f"Prediction result: {result}")

        return jsonify({
            "prediction": float(result[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400