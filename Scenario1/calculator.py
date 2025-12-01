# calculator.py

from fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool(
    name = "multiply",
    description = "Multiplies two numbers.",
    tags = ["arithmetic", "basic math"]
    )
def multiply(x:float, y:float) -> float:
    """
    Multiplies two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The product of the two numbers
    """
    return x * y

@mcp.tool(
    name = "add",
    description = "Adds two numbers.",
    tags = ["arithmetic", "basic math"]
    )
def add(x:float, y:float) -> float:
    """
    Adds two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The sum of the two numbers
    """
    return x + y

@mcp.tool(
    name = "subtract",
    description = "Subtracts two numbers.",
    tags = ["arithmetic", "basic math"]
    )
def subtract(x:float, y:float) -> float:
    """
    Subtracts two numbers
    
    Args:
        x (float): The first number
        y (float): The second number
    
    Returns:
        float: The difference of the two numbers
    """
    return x - y

@mcp.tool(
    name = "divide",
    description = "Divides two numbers.",
    tags = ["arithmetic", "basic math"]
    )
def divide(x:float, y:float) -> float:
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
    return x / y

if __name__ == "__main__":
    mcp.run() #STDIO by default
