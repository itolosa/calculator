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


def cos(x: float) -> float:
    """Calculate the cosine of x (in radians).

    Args:
        x: The angle in radians.

    Returns:
        The cosine of x.
    """
    return math.cos(x)


def sin(x: float) -> float:
    """Calculate the sine of x (in radians).

    Args:
        x: The angle in radians.

    Returns:
        The sine of x.
    """
    return math.sin(x)


def tan(x: float) -> float:
    """Calculate the tangent of x (in radians).

    Args:
        x: The angle in radians.

    Returns:
        The tangent of x.
    """
    return math.tan(x)


def exp(x: float) -> float:
    """Calculate e raised to the power of x.

    Args:
        x: The exponent.

    Returns:
        e raised to the power of x.
    """
    return math.exp(x)


def pow(base: float, exponent: float) -> float:
    """Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        The result of base raised to the power of exponent.
    """
    return base ** exponent


def ln(x: float) -> float:
    """Calculate the natural logarithm (base e) of x.

    Args:
        x: The number to calculate the natural logarithm of.

    Returns:
        The natural logarithm of x.

    Raises:
        ValueError: If x is less than or equal to zero.
    """
    if x <= 0:
        raise ValueError("logarithm is not defined for non-positive numbers")
    return math.log(x)


def log(x: float, base: float = 10.0) -> float:
    """Calculate the logarithm of x with the specified base.

    Args:
        x: The number to calculate the logarithm of.
        base: The base of the logarithm (default is 10).

    Returns:
        The logarithm of x with the specified base.

    Raises:
        ValueError: If x is less than or equal to zero.
        ValueError: If base is less than or equal to zero or equals 1.
    """
    if x <= 0:
        raise ValueError("logarithm is not defined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("logarithm base must be positive and not equal to 1")
    return math.log(x, base)


# Mathematical constants
PI = math.pi
E = math.e
