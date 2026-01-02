from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/predict",methods =['POST'])
def predict_performance_student():
    payload = request.get_json()
    data1 = payload.get("data1")
    data2 = payload.get("data2")
    return jsonify({
        "data1": data1,
        "data2" :data2
    })