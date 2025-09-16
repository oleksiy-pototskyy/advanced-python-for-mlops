#!/usr/bin/python3
"""
Building an API with Flask
Demonstrates creating a REST API endpoint that processes JSON data
and returns JSON responses - foundation for ML prediction APIs
"""

from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """API endpoint that accepts JSON data and returns processed result"""
    # Extract JSON data from request
    data = request.get_json()
    
    # Process the input data (simple sum calculation)
    numbers = data.get("values", [])
    result = sum(numbers)
    
    # Return JSON response
    return jsonify({"sum": result})

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)


