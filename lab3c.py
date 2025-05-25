#!/usr/bin/env python3

"""
lab3c.py

Define the operate() function for OPS445 Lab 3, Investigation 2 - Part 1.
"""

def operate(a, b, operator):
    """Perform the requested operation on two numbers.

    operator must be one of: 'add', 'subtract', 'multiply'.
    Returns an error message string for unsupported operators.
    """
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    else:
        # Unsupported operator: return an error message instead of raising
        return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == "__main__":
    # Example usage
    print(operate(10, 5, 'add'))       # 15
    print(operate(10, 5, 'subtract'))  # 5
    print(operate(10, 5, 'multiply'))  # 50
    print(operate(5, 50, 'divide'))    # Error message

