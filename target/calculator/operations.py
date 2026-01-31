"""Calculator operations module.

This module provides basic arithmetic and scientific operations.
"""

import math


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        The result of base raised to the power of exponent.
    """
    return base ** exponent


def sqrt(n: float) -> float:
    """Calculate the square root of n.

    Args:
        n: The number to calculate the square root of.

    Returns:
        The square root of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("cannot calculate square root of negative number")
    return math.sqrt(n)


def modulo(a: float, b: float) -> float:
    """Calculate the modulus of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The remainder of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b


def factorial(n: int) -> int:
    """Calculate the factorial of n.

    Args:
        n: The non-negative integer to calculate the factorial of.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
        ValueError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("factorial requires an integer input")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    return math.factorial(n)
