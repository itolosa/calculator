"""Tests for calculator operations module."""

import pytest

from calculator.operations import (
    add,
    divide,
    factorial,
    modulo,
    multiply,
    power,
    sqrt,
    subtract,
)


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2.0, 3.0) == 5.0

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2.0, -3.0) == -5.0

    def test_add_positive_and_negative(self):
        """Test adding a positive and negative number."""
        assert add(5.0, -3.0) == 2.0

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(5.0, 0.0) == 5.0
        assert add(0.0, 5.0) == 5.0

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1e100, 2e100) == pytest.approx(3e100)


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5.0, 3.0) == 2.0

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5.0, -3.0) == -2.0

    def test_subtract_positive_and_negative(self):
        """Test subtracting a negative from a positive."""
        assert subtract(5.0, -3.0) == 8.0

    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        assert subtract(5.0, 0.0) == 5.0
        assert subtract(0.0, 5.0) == -5.0

    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        assert subtract(3e100, 1e100) == pytest.approx(2e100)


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3.0, 4.0) == 12.0

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-3.0, -4.0) == 12.0

    def test_multiply_positive_and_negative(self):
        """Test multiplying a positive and negative number."""
        assert multiply(3.0, -4.0) == -12.0

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(5.0, 0.0) == 0.0
        assert multiply(0.0, 5.0) == 0.0

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        assert multiply(1e50, 2e50) == pytest.approx(2e100)


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10.0, 2.0) == 5.0

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-10.0, -2.0) == 5.0

    def test_divide_positive_and_negative(self):
        """Test dividing a positive by a negative number."""
        assert divide(10.0, -2.0) == -5.0

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0.0, 5.0) == 0.0

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(5.0, 0.0)

    def test_divide_large_numbers(self):
        """Test dividing large numbers."""
        assert divide(4e100, 2e100) == 2.0


class TestPower:
    """Tests for the power function."""

    def test_power_positive_base_and_exponent(self):
        """Test raising a positive base to a positive exponent."""
        assert power(2.0, 3.0) == 8.0

    def test_power_negative_base_positive_exponent(self):
        """Test raising a negative base to a positive exponent."""
        assert power(-2.0, 3.0) == -8.0

    def test_power_positive_base_negative_exponent(self):
        """Test raising a positive base to a negative exponent."""
        assert power(2.0, -2.0) == 0.25

    def test_power_base_zero(self):
        """Test raising zero to a positive exponent."""
        assert power(0.0, 5.0) == 0.0

    def test_power_exponent_zero(self):
        """Test raising a number to the power of zero."""
        assert power(5.0, 0.0) == 1.0

    def test_power_fractional_exponent(self):
        """Test raising a base to a fractional exponent."""
        assert power(4.0, 0.5) == 2.0

    def test_power_large_numbers(self):
        """Test raising a base to a large exponent."""
        assert power(10.0, 10.0) == 1e10


class TestSqrt:
    """Tests for the sqrt function."""

    def test_sqrt_positive_number(self):
        """Test square root of a positive number."""
        assert sqrt(4.0) == 2.0

    def test_sqrt_zero(self):
        """Test square root of zero."""
        assert sqrt(0.0) == 0.0

    def test_sqrt_large_number(self):
        """Test square root of a large number."""
        assert sqrt(1e100) == 1e50

    def test_sqrt_fractional_number(self):
        """Test square root of a fractional number."""
        assert sqrt(0.25) == 0.5

    def test_sqrt_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(
            ValueError, match="cannot calculate square root of negative number"
        ):
            sqrt(-1.0)

    def test_sqrt_perfect_square(self):
        """Test square root of perfect squares."""
        assert sqrt(9.0) == 3.0
        assert sqrt(16.0) == 4.0
        assert sqrt(25.0) == 5.0


class TestModulo:
    """Tests for the modulo function."""

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        assert modulo(10.0, 3.0) == 1.0

    def test_modulo_negative_dividend(self):
        """Test modulo with negative dividend."""
        assert modulo(-10.0, 3.0) == 2.0

    def test_modulo_negative_divisor(self):
        """Test modulo with negative divisor."""
        assert modulo(10.0, -3.0) == -2.0

    def test_modulo_zero_dividend(self):
        """Test modulo with zero dividend."""
        assert modulo(0.0, 5.0) == 0.0

    def test_modulo_by_zero_raises_error(self):
        """Test that modulo by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="modulo by zero"):
            modulo(5.0, 0.0)

    def test_modulo_exact_division(self):
        """Test modulo when dividend is exactly divisible."""
        assert modulo(10.0, 5.0) == 0.0

    def test_modulo_fractional_numbers(self):
        """Test modulo with fractional numbers."""
        result = modulo(5.5, 2.0)
        assert abs(result - 1.5) < 1e-10


class TestFactorial:
    """Tests for the factorial function."""

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1

    def test_factorial_small_positive(self):
        """Test factorial of small positive numbers."""
        assert factorial(5) == 120
        assert factorial(6) == 720

    def test_factorial_ten(self):
        """Test factorial of ten."""
        assert factorial(10) == 3628800

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(
            ValueError, match="factorial is not defined for negative numbers"
        ):
            factorial(-1)

    def test_factorial_non_integer_raises_error(self):
        """Test that factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError, match="factorial requires an integer input"):
            factorial(5.5)

    def test_factorial_large_number(self):
        """Test factorial of a larger number."""
        assert factorial(12) == 479001600
