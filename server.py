import os
from fastmcp import FastMCP

mcp = FastMCP(
    name="AdditionServer",
    instructions="This server adds two numbers.",
    sse_path="/calculator/sse",
    message_path="/calculator/messages/",
)

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract two numbers and return the result."""
    return a - b

@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers and return the result."""
    return a / b


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8001"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
