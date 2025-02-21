from flask import Flask, render_template, request, send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder="frontend", template_folder="frontend")

# Load the trained model
model_path = "/Users/vaibhavgautam/Documents/VS CODE/PYTHON_Scripts/Placement-Predictor/model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            iq = float(request.form["iq"])

            # Predict using the model
            result = model.predict(np.array([[cgpa, iq]]))[0]
            prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

# Serve static files like CSS and JS
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("frontend", filename)

if __name__ == "__main__":
    app.run(debug=True)