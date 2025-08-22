from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)
util.load_saved_artifacts()

@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    return jsonify({"locations": util.get_location_names()})

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json(silent=True)
    if not data:
        data = request.form.to_dict()

    missing = [k for k in ["location", "sqft", "broom","bath"] if k not in data]
    if missing:
        return jsonify({"error": f"Faltan campos: {', '.join(missing)}"}), 400

    try:
        price = util.get_estimated_price(
            location=data["location"],
            sqft=float(data["sqft"]),
            broom=int(data["broom"]),
            bath=int(data["bath"])
        )
    except Exception as e:
        return jsonify({"error": f"Entrada inválida: {e}"}), 400

    return jsonify({"estimated_price": price})


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    app.run(debug=False)

