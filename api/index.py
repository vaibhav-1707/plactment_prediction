import json
import urllib.parse

def handler(event, context):
    method = event.get("method", "GET")
    path = event.get("path", "/")
    body = event.get("body", "")

    if method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": get_html_form()
        }

    elif method == "POST":
        if path == "/predict":  # JSON API
            try:
                data = json.loads(body)
                cgpa = float(data.get('cgpa', 0))
                iq = float(data.get('iq', 0))
                result = predict_placement(cgpa, iq)
                prediction = "Will be placed" if result == 1 else "Will not be placed"

                return {
                    "statusCode": 200,
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({
                        "prediction": prediction,
                        "placed": bool(result)
                    })
                }
            except Exception as e:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({"error": str(e)})
                }

        else:  # Handle HTML form submission
            form_data = parse_form_data(body)
            try:
                cgpa = float(form_data.get('cgpa', 0))
                iq = float(form_data.get('iq', 0))
                result = predict_placement(cgpa, iq)
                prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"

                return {
                    "statusCode": 200,
                    "headers": {"Content-Type": "text/html"},
                    "body": get_html_form(prediction)
                }
            except Exception as e:
                return {
                    "statusCode": 500,
                    "headers": {"Content-Type": "text/html"},
                    "body": get_html_form(f"Error: {str(e)}")
                }

    return {
        "statusCode": 404,
        "headers": {"Content-Type": "text/plain"},
        "body": "Not Found"
    }


def predict_placement(cgpa, iq):
    if cgpa >= 8.0 and iq >= 120:
        return 1
    elif cgpa >= 7.0 and iq >= 110:
        return 1
    elif cgpa >= 6.5 and iq >= 100:
        return 1
    else:
        return 0


def parse_form_data(data):
    form_data = {}
    if data:
        pairs = data.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                form_data[key] = urllib.parse.unquote_plus(value)
    return form_data


def get_html_form(prediction=None):
    prediction_html = ""
    if prediction:
        css_class = "success" if "✅" in prediction else "error"
        prediction_html = f'<div class="prediction {css_class}">{prediction}</div>'
    
    return f"""
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
            input {{ width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }}
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
            {prediction_html}
        </div>
    </body>
    </html>
    """
