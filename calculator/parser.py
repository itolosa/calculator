"""Mathematical expression parser with operator precedence support.

This module implements a recursive descent parser for evaluating mathematical
expressions without using eval() or exec().
"""

from typing import Union


class Tokenizer:
    """Tokenizer for mathematical expressions."""

    def __init__(self, expression: str):
        self.expression = expression
        self.pos = 0
        self.length = len(self.expression)

    def skip_whitespace(self) -> None:
        """Skip whitespace characters."""
        while self.pos < self.length and self.expression[self.pos] in (' ', '\t', '\n', '\r'):
            self.pos += 1

    def peek(self) -> str:
        """Peek at the current character without consuming it."""
        self.skip_whitespace()
        if self.pos < self.length:
            return self.expression[self.pos]
        return ""

    def advance(self) -> str:
        """Consume and return the current character."""
        char = self.peek()
        self.pos += 1
        return char

    def parse_number(self) -> float:
        """Parse a number (integer or decimal)."""
        self.skip_whitespace()
        start = self.pos

        # Handle negative numbers
        if self.pos < self.length and self.expression[self.pos] == '-':
            self.pos += 1

        # Parse digits before decimal point
        if self.pos >= self.length or (not self.expression[self.pos].isdigit() and self.expression[self.pos] != '.'):
            raise SyntaxError(f"Expected number at position {self.pos}")

        while self.pos < self.length and self.expression[self.pos].isdigit():
            self.pos += 1

        # Parse decimal point and fractional part
        if self.pos < self.length and self.expression[self.pos] == '.':
            self.pos += 1
            if self.pos >= self.length or not self.expression[self.pos].isdigit():
                raise SyntaxError(f"Expected digit after decimal point at position {self.pos}")
            while self.pos < self.length and self.expression[self.pos].isdigit():
                self.pos += 1

        number_str = self.expression[start:self.pos]
        return float(number_str)


class Parser:
    """Recursive descent parser for mathematical expressions.

    Grammar:
        expression := term (('+' | '-') term)*
        term       := factor (('*' | '/') factor)*
        factor     := number | '(' expression ')' | '-' factor
    """

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def parse_expression(self) -> float:
        """Parse an expression (handles + and -)."""
        result = self.parse_term()

        while self.tokenizer.peek() in ('+', '-'):
            op = self.tokenizer.advance()
            right = self.parse_term()
            if op == '+':
                result += right
            else:
                result -= right

        return result

    def parse_term(self) -> float:
        """Parse a term (handles * and /)."""
        result = self.parse_factor()

        while self.tokenizer.peek() in ('*', '/'):
            op = self.tokenizer.advance()
            right = self.parse_factor()
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division by zero in expression")
                result /= right

        return result

    def parse_factor(self) -> float:
        """Parse a factor (number, parenthesized expression, or unary minus)."""
        char = self.tokenizer.peek()

        # Handle parentheses
        if char == '(':
            self.tokenizer.advance()
            result = self.parse_expression()
            if self.tokenizer.peek() != ')':
                raise SyntaxError(f"Expected ')' at position {self.tokenizer.pos}")
            self.tokenizer.advance()
            return result

        # Handle unary minus
        if char == '-':
            self.tokenizer.advance()
            return -self.parse_factor()

        # Handle numbers
        if char.isdigit() or char == '.':
            return self.tokenizer.parse_number()

        # Invalid character
        if char == '':
            raise SyntaxError("Unexpected end of expression")
        raise SyntaxError(f"Unexpected character '{char}' at position {self.tokenizer.pos}")


def parse_and_evaluate(expression: str) -> float:
    """Parse and evaluate a mathematical expression.

    Args:
        expression: A string containing a mathematical expression with
                   operators +, -, *, /, parentheses, and numbers.

    Returns:
        The result of evaluating the expression as a float.

    Raises:
        SyntaxError: If the expression is malformed.
        ZeroDivisionError: If the expression contains division by zero.

    Examples:
        >>> parse_and_evaluate("2 + 3")
        5.0
        >>> parse_and_evaluate("(2 + 3) * 4")
        20.0
        >>> parse_and_evaluate("-5 + 3")
        -2.0
        >>> parse_and_evaluate("3.14 * 2")
        6.28
    """
    if not expression or not expression.strip():
        raise SyntaxError("Empty expression")

    tokenizer = Tokenizer(expression)
    parser = Parser(tokenizer)
    result = parser.parse_expression()

    # Check if there are any unconsumed characters
    if tokenizer.peek():
        raise SyntaxError(f"Unexpected character '{tokenizer.peek()}' at position {tokenizer.pos}")

    return result
