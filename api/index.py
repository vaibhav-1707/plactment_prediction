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
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            iq = float(request.form["iq"])

            # Predict using simple logic
            result = predict_placement(cgpa, iq)
            prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"

        except Exception as e:
            prediction = f"Error: {str(e)}"
    else:
        prediction = None

    # Return simple HTML instead of template
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Placement Prediction</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }}
            .container {{ background: #f5f5f5; padding: 30px; border-radius: 10px; }}
            h1 {{ color: #333; text-align: center; }}
            .form-group {{ margin: 15px 0; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; }}
            input {{ width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }}
            button {{ background: #007bff; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; width: 100%; }}
            button:hover {{ background: #0056b3; }}
            .prediction {{ margin-top: 20px; padding: 15px; border-radius: 5px; text-align: center; font-weight: bold; }}
            .success {{ background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }}
            .error {{ background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎯 Placement Prediction</h1>
            <form method="POST">
                <div class="form-group">
                    <label for="cgpa">CGPA (0-10):</label>
                    <input type="number" id="cgpa" name="cgpa" step="0.1" min="0" max="10" required>
                </div>
                <div class="form-group">
                    <label for="iq">IQ Score:</label>
                    <input type="number" id="iq" name="iq" min="50" max="200" required>
                </div>
                <button type="submit">🔮 Predict Placement</button>
            </form>
            {f'<div class="prediction {"success" if prediction and "✅" in prediction else "error" if prediction else ""}">{prediction}</div>' if prediction else ''}
        </div>
    </body>
    </html>
    """
    return html

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