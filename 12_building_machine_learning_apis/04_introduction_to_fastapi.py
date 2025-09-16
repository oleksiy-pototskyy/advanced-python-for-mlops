#!/usr/bin/python3
"""
Introduction to FastAPI
Demonstrates FastAPI framework with automatic data validation
and type hints - modern approach for building ML APIs
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI()

class InputData(BaseModel):
    """Pydantic model for request data validation"""
    values: list[int]

@app.post("/predict")
def predict(data: InputData):
    """API endpoint with automatic type validation and JSON serialization"""
    # Process validated input data
    result = sum(data.values)
    
    # Return response (automatically converted to JSON)
    return {"sum": result}

# Run with: uvicorn filename:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

