"""Tests for the calculator evaluator."""

import unittest
from calculator.evaluator import evaluate


class TestEvaluator(unittest.TestCase):
    """Test cases for the evaluate function."""

    def test_simple_addition(self):
        """Test simple addition."""
        self.assertEqual(evaluate("2 + 3"), 5.0)

    def test_simple_subtraction(self):
        """Test simple subtraction."""
        self.assertEqual(evaluate("10 - 3"), 7.0)

    def test_simple_multiplication(self):
        """Test simple multiplication."""
        self.assertEqual(evaluate("4 * 5"), 20.0)

    def test_simple_division(self):
        """Test simple division."""
        self.assertEqual(evaluate("10 / 2"), 5.0)

    def test_order_of_operations(self):
        """Test that order of operations is respected."""
        self.assertEqual(evaluate("2 + 3 * 4"), 14.0)
        self.assertEqual(evaluate("10 / 2 * 3"), 15.0)

    def test_parentheses(self):
        """Test expressions with parentheses."""
        self.assertEqual(evaluate("(2 + 3) * 4"), 20.0)
        self.assertEqual(evaluate("2 * (3 + 4)"), 14.0)

    def test_complex_expression(self):
        """Test complex expressions."""
        self.assertEqual(evaluate("(5 + 3) * 2 - 4 / 2"), 14.0)

    def test_negative_numbers(self):
        """Test expressions with negative numbers."""
        self.assertEqual(evaluate("-5 + 3"), -2.0)
        self.assertEqual(evaluate("10 + (-3)"), 7.0)

    def test_floating_point(self):
        """Test floating point numbers."""
        self.assertEqual(evaluate("2.5 + 3.5"), 6.0)
        self.assertAlmostEqual(evaluate("10 / 3"), 3.333333, places=5)

    def test_empty_expression(self):
        """Test that empty expressions raise ValueError."""
        with self.assertRaises(ValueError):
            evaluate("")
        with self.assertRaises(ValueError):
            evaluate("   ")

    def test_division_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            evaluate("10 / 0")

    def test_invalid_syntax(self):
        """Test that invalid syntax raises ValueError."""
        with self.assertRaises(ValueError):
            evaluate("2 +")
        with self.assertRaises(ValueError):
            evaluate("* 3")
        with self.assertRaises(ValueError):
            evaluate("2 + + 3")

    def test_invalid_expression(self):
        """Test that invalid expressions raise ValueError."""
        with self.assertRaises(ValueError):
            evaluate("hello")
        with self.assertRaises(ValueError):
            evaluate("2 + abc")

    def test_whitespace_handling(self):
        """Test that whitespace is handled correctly."""
        self.assertEqual(evaluate("  2  +  3  "), 5.0)
        self.assertEqual(evaluate("2+3"), 5.0)


if __name__ == '__main__':
    unittest.main()
