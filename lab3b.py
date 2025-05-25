#!/usr/bin/env python3

"""
lab3b.py

Define basic arithmetic functions for OPS445 Lab 3, Investigation 2 - Part 1.
"""

def sum_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


if __name__ == "__main__":
    # Example usage
    print(f"Sum: {sum_numbers(10, 5)}")
    print(f"Difference: {subtract_numbers(10, 5)}")
    print(f"Product: {multiply_numbers(10, 5)}")

