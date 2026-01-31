"""Tests for the expression parser."""

import pytest
from calculator.parser import parse_and_evaluate


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_addition(self):
        assert parse_and_evaluate("2 + 3") == 5.0

    def test_subtraction(self):
        assert parse_and_evaluate("10 - 3") == 7.0

    def test_multiplication(self):
        assert parse_and_evaluate("4 * 5") == 20.0

    def test_division(self):
        assert parse_and_evaluate("10 / 2") == 5.0

    def test_decimal_numbers(self):
        assert parse_and_evaluate("3.14 * 2") == pytest.approx(6.28)
        assert parse_and_evaluate("5.5 + 2.5") == pytest.approx(8.0)
        assert parse_and_evaluate("10.0 / 4.0") == pytest.approx(2.5)


class TestOperatorPrecedence:
    """Test that operator precedence is handled correctly."""

    def test_multiplication_before_addition(self):
        assert parse_and_evaluate("2 + 3 * 4") == 14.0

    def test_division_before_subtraction(self):
        assert parse_and_evaluate("10 - 6 / 2") == 7.0

    def test_multiple_operations(self):
        assert parse_and_evaluate("2 + 3 * 4 - 5") == 9.0

    def test_left_to_right_same_precedence(self):
        assert parse_and_evaluate("10 - 5 - 2") == 3.0
        assert parse_and_evaluate("20 / 4 / 2") == pytest.approx(2.5)


class TestParentheses:
    """Test that parentheses override operator precedence."""

    def test_simple_parentheses(self):
        assert parse_and_evaluate("(2 + 3) * 4") == 20.0

    def test_parentheses_with_subtraction(self):
        assert parse_and_evaluate("(10 - 6) / 2") == 2.0

    def test_nested_parentheses(self):
        assert parse_and_evaluate("((2 + 3) * (4 - 1))") == 15.0
        assert parse_and_evaluate("(1 + (2 + (3 + 4)))") == 10.0

    def test_complex_nested_parentheses(self):
        assert parse_and_evaluate("((2 + 3) * 4) - ((5 - 2) * 3)") == 11.0


class TestNegativeNumbers:
    """Test handling of negative numbers."""

    def test_negative_number_at_start(self):
        assert parse_and_evaluate("-5 + 3") == -2.0

    def test_negative_number_standalone(self):
        assert parse_and_evaluate("-10") == -10.0

    def test_negative_in_expression(self):
        assert parse_and_evaluate("5 + -3") == 2.0
        assert parse_and_evaluate("5 * -2") == -10.0

    def test_negative_with_parentheses(self):
        assert parse_and_evaluate("-(5 + 3)") == -8.0
        assert parse_and_evaluate("-(-5)") == 5.0

    def test_negative_decimal(self):
        assert parse_and_evaluate("-3.5 + 1.5") == -2.0


class TestWhitespace:
    """Test that whitespace is handled correctly."""

    def test_spaces_in_expression(self):
        assert parse_and_evaluate("  2  +  3  ") == 5.0
        assert parse_and_evaluate(" ( 2 + 3 ) * 4 ") == 20.0

    def test_no_spaces(self):
        assert parse_and_evaluate("2+3*4") == 14.0
        assert parse_and_evaluate("(2+3)*4") == 20.0


class TestComplexExpressions:
    """Test complex expressions combining multiple features."""

    def test_complex_expression_1(self):
        assert parse_and_evaluate("3 + 4 * 2 / (1 - 5)") == pytest.approx(1.0)

    def test_complex_expression_2(self):
        assert parse_and_evaluate("10 + -5 * 2") == 0.0

    def test_complex_expression_3(self):
        assert parse_and_evaluate("((10 + 5) * 3 - 20) / 5") == pytest.approx(5.0)

    def test_complex_expression_4(self):
        assert parse_and_evaluate("-(-(-1))") == -1.0


class TestErrorHandling:
    """Test that malformed expressions raise appropriate errors."""

    def test_empty_expression(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("")

    def test_whitespace_only(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("   ")

    def test_missing_operand_at_end(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 +")

    def test_missing_operand_at_start(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("* 3")

    def test_consecutive_operators(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 * * 3")

    def test_consecutive_numbers(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 3")

    def test_missing_closing_parenthesis(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("(2 + 3")

    def test_missing_opening_parenthesis(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 + 3)")

    def test_empty_parentheses(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("()")

    def test_invalid_character(self):
        with pytest.raises(SyntaxError):
            parse_and_evaluate("2 + a")


class TestDivisionByZero:
    """Test that division by zero raises appropriate error."""

    def test_simple_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            parse_and_evaluate("5 / 0")

    def test_division_by_zero_in_expression(self):
        with pytest.raises(ZeroDivisionError):
            parse_and_evaluate("10 + 5 / 0")

    def test_division_by_zero_expression(self):
        with pytest.raises(ZeroDivisionError):
            parse_and_evaluate("10 / (5 - 5)")


class TestNoEvalUsed:
    """Verify that eval() or exec() are not used in the implementation."""

    def test_no_eval_in_parser_module(self):
        import calculator.parser
        import ast
        import inspect

        # Use AST to check for actual function calls, not just text in docstrings
        source = inspect.getsource(calculator.parser)
        tree = ast.parse(source)

        # Walk through all nodes and check for Call nodes
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check if the function being called is 'eval' or 'exec'
                if isinstance(node.func, ast.Name):
                    assert node.func.id not in ('eval', 'exec'), \
                        f"Implementation must not use {node.func.id}()"
