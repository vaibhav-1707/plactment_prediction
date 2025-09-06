from flask import Flask, render_template, request, jsonify
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

# Simple prediction logic (replaces ML model for deployment)
def predict_placement(cgpa, iq):
    """
    Simple prediction logic based on CGPA and IQ scores
    This replaces the ML model for Vercel deployment
    """
    # Simple rule-based prediction
    if cgpa >= 8.0 and iq >= 120:
        return 1  # Will be placed
    elif cgpa >= 7.0 and iq >= 110:
        return 1  # Will be placed
    elif cgpa >= 6.5 and iq >= 100:
        return 1  # Will be placed
    else:
        return 0  # Will not be placed

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            iq = float(request.form["iq"])

            # Predict using simple logic
            result = predict_placement(cgpa, iq)
            prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        cgpa = float(data["cgpa"])
        iq = float(data["iq"])
        
        # Predict using simple logic
        result = predict_placement(cgpa, iq)
        prediction = "Will be placed" if result == 1 else "Will not be placed"
        
        return jsonify({
            "prediction": prediction,
            "placed": bool(result)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Apply ProxyFix to handle Vercel's proxying
app.wsgi_app = ProxyFix(app.wsgi_app)

# Vercel serverless function handler
def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    app.run(debug=True)