import json
import os

def handler(request):
    """
    Simple HTTP handler for Vercel
    """
    try:
        # Get the request method and path
        method = request.get('REQUEST_METHOD', 'GET')
        path = request.get('PATH_INFO', '/')
        
        # Handle different routes
        if path == '/' and method == 'GET':
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/html',
                },
                'body': get_html_form()
            }
        
        elif path == '/' and method == 'POST':
            # Parse form data
            content_length = int(request.get('CONTENT_LENGTH', 0))
            if content_length > 0:
                post_data = request.get('wsgi.input', '').read(content_length).decode('utf-8')
                form_data = parse_form_data(post_data)
                
                try:
                    cgpa = float(form_data.get('cgpa', 0))
                    iq = float(form_data.get('iq', 0))
                    
                    # Simple prediction logic
                    result = predict_placement(cgpa, iq)
                    prediction = "✅ Will be placed" if result == 1 else "❌ Will not be placed"
                    
                    return {
                        'statusCode': 200,
                        'headers': {
                            'Content-Type': 'text/html',
                        },
                        'body': get_html_form(prediction)
                    }
                except Exception as e:
                    return {
                        'statusCode': 200,
                        'headers': {
                            'Content-Type': 'text/html',
                        },
                        'body': get_html_form(f"Error: {str(e)}")
                    }
        
        elif path == '/predict' and method == 'POST':
            # Handle JSON API
            content_length = int(request.get('CONTENT_LENGTH', 0))
            if content_length > 0:
                post_data = request.get('wsgi.input', '').read(content_length).decode('utf-8')
                data = json.loads(post_data)
                
                try:
                    cgpa = float(data.get('cgpa', 0))
                    iq = float(data.get('iq', 0))
                    
                    result = predict_placement(cgpa, iq)
                    prediction = "Will be placed" if result == 1 else "Will not be placed"
                    
                    return {
                        'statusCode': 200,
                        'headers': {
                            'Content-Type': 'application/json',
                        },
                        'body': json.dumps({
                            'prediction': prediction,
                            'placed': bool(result)
                        })
                    }
                except Exception as e:
                    return {
                        'statusCode': 400,
                        'headers': {
                            'Content-Type': 'application/json',
                        },
                        'body': json.dumps({'error': str(e)})
                    }
        
        # Default response
        return {
            'statusCode': 404,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': '<h1>404 - Not Found</h1>'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': f'<h1>500 - Server Error</h1><p>{str(e)}</p>'
        }

def predict_placement(cgpa, iq):
    """
    Simple prediction logic based on CGPA and IQ scores
    """
    if cgpa >= 8.0 and iq >= 120:
        return 1  # Will be placed
    elif cgpa >= 7.0 and iq >= 110:
        return 1  # Will be placed
    elif cgpa >= 6.5 and iq >= 100:
        return 1  # Will be placed
    else:
        return 0  # Will not be placed

def parse_form_data(data):
    """
    Parse form data from POST request
    """
    form_data = {}
    if data:
        pairs = data.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                form_data[key] = value.replace('+', ' ')
    return form_data

def get_html_form(prediction=None):
    """
    Generate HTML form
    """
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