"""Tests for calculator operations module."""

import pytest

from calculator.operations import add, divide, multiply, subtract


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
        assert add(1e100, 2e100) == 3e100


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
        assert subtract(3e100, 1e100) == 2e100


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
        assert multiply(1e50, 2e50) == 2e100


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
