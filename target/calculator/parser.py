"""Calculator parser module.

This module handles parsing of calculator expressions.
"""

import operator
import re


class Parser:
    """Expression parser for calculator."""

    def __init__(self):
        """Initialize the parser."""
        self.operators = {
            '+': (1, operator.add),
            '-': (1, operator.sub),
            '*': (2, operator.mul),
            '/': (2, operator.truediv),
        }

    def parse(self, expression: str) -> float:
        """Parse and evaluate a mathematical expression.

        Args:
            expression: The mathematical expression to evaluate.

        Returns:
            The result of the expression.

        Raises:
            SyntaxError: If the expression is malformed.
            ZeroDivisionError: If division by zero occurs.
        """
        if not expression or not expression.strip():
            raise SyntaxError("empty expression")

        expression = expression.strip()

        try:
            result = self._evaluate(expression)
            return float(result)
        except ZeroDivisionError:
            raise
        except Exception as e:
            raise SyntaxError(f"invalid expression: {e}")

    def _evaluate(self, expression: str) -> float:
        """Evaluate an expression using the shunting yard algorithm.

        Args:
            expression: The expression to evaluate.

        Returns:
            The result of the evaluation.
        """
        output_queue = []
        operator_stack = []

        tokens = self._tokenize(expression)

        for token in tokens:
            if self._is_number(token):
                output_queue.append(float(token))
            elif token in self.operators:
                while (
                    operator_stack
                    and operator_stack[-1] != '('
                    and operator_stack[-1] in self.operators
                    and self.operators[operator_stack[-1]][0]
                    >= self.operators[token][0]
                ):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise SyntaxError("mismatched parentheses")
                operator_stack.pop()
            else:
                raise SyntaxError(f"invalid token: {token}")

        while operator_stack:
            op = operator_stack.pop()
            if op in ('(', ')'):
                raise SyntaxError("mismatched parentheses")
            output_queue.append(op)

        return self._evaluate_rpn(output_queue)

    def _tokenize(self, expression: str) -> list:
        """Tokenize an expression.

        Args:
            expression: The expression to tokenize.

        Returns:
            A list of tokens.
        """
        pattern = r'(\d+\.?\d*|\+|\-|\*|\/|\(|\))'
        tokens = re.findall(pattern, expression)

        processed_tokens = []
        for i, token in enumerate(tokens):
            if token == '-' and (i == 0 or tokens[i-1] in ('(', '+', '-', '*', '/')):
                if i + 1 < len(tokens) and self._is_number(tokens[i + 1]):
                    processed_tokens.append('-' + tokens[i + 1])
                    tokens[i + 1] = ''
            elif token:
                processed_tokens.append(token)

        return [t for t in processed_tokens if t]

    def _is_number(self, token: str) -> bool:
        """Check if a token is a number.

        Args:
            token: The token to check.

        Returns:
            True if the token is a number, False otherwise.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _evaluate_rpn(self, tokens: list) -> float:
        """Evaluate tokens in Reverse Polish Notation.

        Args:
            tokens: The tokens to evaluate.

        Returns:
            The result of the evaluation.
        """
        stack = []

        for token in tokens:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in self.operators:
                if len(stack) < 2:
                    raise SyntaxError("invalid expression")
                b = stack.pop()
                a = stack.pop()
                _, op_func = self.operators[token]
                result = op_func(a, b)
                stack.append(result)

        if len(stack) != 1:
            raise SyntaxError("invalid expression")

        return stack[0]


def parse(expression: str) -> float:
    """Parse and evaluate a mathematical expression.

    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The result of the expression.

    Raises:
        SyntaxError: If the expression is malformed.
        ZeroDivisionError: If division by zero occurs.
    """
    parser = Parser()
    return parser.parse(expression)


def parse_and_evaluate(expression: str) -> float:
    """Parse and evaluate a mathematical expression.

    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The result of the expression.

    Raises:
        SyntaxError: If the expression is malformed.
        ZeroDivisionError: If division by zero occurs.
    """
    return parse(expression)
