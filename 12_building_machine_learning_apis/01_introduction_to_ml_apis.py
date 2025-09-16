#!/usr/bin/python3
"""
Introduction to ML APIs
Demonstrates building a simple machine learning API using Flask
for serving model predictions in production environments
"""

from flask import Flask, request, jsonify
import joblib

# Create Flask application for ML model serving
app = Flask(__name__)

# Load pre-trained model (assumes model.pkl exists)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    """ML prediction endpoint - core API functionality"""
    # Get input features from JSON request
    data = request.json
    
    # Make prediction using loaded model
    prediction = model.predict([data["features"]])
    
    # Return prediction as JSON response
    return jsonify({"prediction": prediction.tolist()})

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
