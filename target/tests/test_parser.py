"""Tests for calculator parser module."""

import pytest

from calculator.parser import parse, parse_and_evaluate


class TestSimpleExpressions:
    """Tests for simple arithmetic expressions."""

    def test_simple_addition(self):
        """Test simple addition."""
        assert parse("2 + 3") == 5.0

    def test_simple_subtraction(self):
        """Test simple subtraction."""
        assert parse("10 - 4") == 6.0

    def test_simple_multiplication(self):
        """Test simple multiplication."""
        assert parse("3 * 5") == 15.0

    def test_simple_division(self):
        """Test simple division."""
        assert parse("8 / 2") == 4.0


class TestOperatorPrecedence:
    """Tests for operator precedence."""

    def test_addition_and_multiplication(self):
        """Test that multiplication has higher precedence than addition."""
        assert parse("2 + 3 * 4") == 14.0

    def test_multiplication_and_subtraction(self):
        """Test that multiplication has higher precedence than subtraction."""
        assert parse("10 - 2 * 3") == 4.0

    def test_division_and_addition(self):
        """Test that division has higher precedence than addition."""
        assert parse("10 + 6 / 2") == 13.0


class TestParentheses:
    """Tests for parentheses."""

    def test_simple_parentheses(self):
        """Test simple parentheses."""
        assert parse("(2 + 3) * 4") == 20.0

    def test_nested_parentheses(self):
        """Test nested parentheses."""
        assert parse("((1 + 2) * (3 + 4))") == 21.0

    def test_multiple_groups(self):
        """Test multiple groups of parentheses."""
        assert parse("(2 + 3) * (4 + 5)") == 45.0

    def test_parentheses_with_division(self):
        """Test parentheses with division."""
        assert parse("(10 + 2) / 3") == 4.0


class TestNegativeNumbers:
    """Tests for negative numbers."""

    def test_negative_number_addition(self):
        """Test addition with negative number."""
        assert parse("-5 + 3") == -2.0

    def test_negative_number_subtraction(self):
        """Test subtraction with negative number."""
        assert parse("-5 - 3") == -8.0

    def test_negative_number_multiplication(self):
        """Test multiplication with negative number."""
        assert parse("-5 * 2") == -10.0

    def test_two_negative_numbers(self):
        """Test operation with two negative numbers."""
        assert parse("-5 + -3") == -8.0


class TestDecimalNumbers:
    """Tests for decimal numbers."""

    def test_decimal_multiplication(self):
        """Test multiplication with decimal number."""
        assert parse("3.14 * 2") == pytest.approx(6.28)

    def test_decimal_addition(self):
        """Test addition with decimal numbers."""
        assert parse("1.5 + 2.5") == 4.0

    def test_decimal_division(self):
        """Test division with decimal numbers."""
        assert parse("7.5 / 2.5") == 3.0


class TestComplexExpressions:
    """Tests for complex expressions."""

    def test_complex_expression_1(self):
        """Test complex expression with multiple operators."""
        assert parse("2 + 3 * 4 - 5") == 9.0

    def test_complex_expression_2(self):
        """Test complex expression with parentheses and multiple operators."""
        assert parse("(2 + 3) * (4 - 1)") == 15.0

    def test_complex_expression_3(self):
        """Test complex expression with division and subtraction."""
        assert parse("10 / 2 + 3 * 2") == 11.0


class TestErrorHandling:
    """Tests for error handling."""

    def test_empty_expression(self):
        """Test that empty expression raises SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("")

    def test_whitespace_only(self):
        """Test that whitespace-only expression raises SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("   ")

    def test_mismatched_opening_parenthesis(self):
        """Test that mismatched opening parenthesis raises SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("(2 + 3")

    def test_mismatched_closing_parenthesis(self):
        """Test that mismatched closing parenthesis raises SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("2 + 3)")

    def test_division_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            parse("5 / 0")

    def test_invalid_characters(self):
        """Test that invalid characters raise SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("2 + a")

    def test_consecutive_operators(self):
        """Test that consecutive operators raise SyntaxError."""
        with pytest.raises(SyntaxError):
            parse("2 + * 3")


class TestParseAndEvaluate:
    """Tests for parse_and_evaluate function."""

    def test_basic_expression(self):
        """Test that parse_and_evaluate works for basic expressions."""
        assert parse_and_evaluate("2 + 3") == 5.0

    def test_operator_precedence(self):
        """Test that parse_and_evaluate respects operator precedence."""
        assert parse_and_evaluate("2 + 3 * 4") == 14.0

    def test_parentheses(self):
        """Test that parse_and_evaluate handles parentheses."""
        assert parse_and_evaluate("(2 + 3) * 4") == 20.0

    def test_negative_numbers(self):
        """Test that parse_and_evaluate handles negative numbers."""
        assert parse_and_evaluate("-5 + 3") == -2.0

    def test_decimal_numbers(self):
        """Test that parse_and_evaluate handles decimal numbers."""
        assert parse_and_evaluate("3.14 * 2") == pytest.approx(6.28)

    def test_nested_parentheses(self):
        """Test that parse_and_evaluate handles nested parentheses."""
        assert parse_and_evaluate("((2 + 3) * (4 - 1))") == 15.0

    def test_malformed_expression(self):
        """Test that parse_and_evaluate raises SyntaxError for malformed expressions."""
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 +")

    def test_division_by_zero(self):
        """Test that parse_and_evaluate raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            parse_and_evaluate("5 / 0")
