#!/usr/bin/python3
"""
Building an API with FastAPI
Demonstrates creating a complete FastAPI endpoint with
type validation and automatic documentation generation
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application with automatic docs
app = FastAPI()

class InputData(BaseModel):
    """Input schema with type validation"""
    x: float
    y: float

@app.post("/add")
def add_numbers(data: InputData):
    """Add two numbers - demonstrates ML-style computation endpoint"""
    # Perform calculation on validated input
    result = data.x + data.y
    
    # Return structured response
    return {"sum": result}

# Run with: uvicorn filename:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


