# calculator_api.py

import uvicorn

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1. Create FastAPI instance
app = FastAPI(title="CalculatorAPI")

@app.post("/multiply")
def multiply_numbers(x:float, y:float) -> dict[str, float]:
    """
    Multiplies two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The product of the two numbers
    """
    return {"Result": x * y}

@app.post("/add")
def add_numbers(x:float, y:float) -> dict[str, float]:
    """
    Adds two numbers

    Args:
        x (float): The first number
        y (float): The second number

    Returns:
        float: The sum of the two numbers
    """
    return {"Result": x + y}

@app.post("/subtract")
def subtract_numbers(x:float, y:float) -> dict[str, float]:
    """
    Subtracts two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The difference of the two numbers
    """
    return {"Result": x - y}

@app.post("/divide")
def divide_numbers(x:float, y:float) -> dict[str, float]:
    """
    Divides two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The quotient of the two numbers
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return {"Result": x / y}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
