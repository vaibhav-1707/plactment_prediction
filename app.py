from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder="frontend", template_folder="frontend")

# Load the trained model
model_path = "model.pkl"
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"Model file '{model_path}' not found.")
    model = None

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            if model is None:
                prediction = "❌ Model not loaded. Please check if model.pkl exists."
            else:
                cgpa = float(request.form["cgpa"])
                iq = float(request.form["iq"])

                # Predict using the model
                result = model.predict(np.array([[cgpa, iq]]))[0]
                prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        data = request.get_json()
        cgpa = float(data["cgpa"])
        iq = float(data["iq"])
        
        # Predict using the model
        result = model.predict(np.array([[cgpa, iq]]))[0]
        prediction = "Will be placed" if result == 1 else "Will not be placed"
        
        return jsonify({
            "prediction": prediction,
            "placed": bool(result)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
