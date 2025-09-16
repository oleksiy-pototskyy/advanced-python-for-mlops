#!/usr/bin/python3
"""
Introduction to Flask Framework
Demonstrates basic Flask web application setup
for building ML APIs and web services
"""

from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route("/")
def home():
    """Basic route handler - returns simple text response"""
    return "Hello, Flask is running!"

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)



