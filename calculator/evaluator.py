"""Expression evaluator for the calculator."""


def evaluate(expression: str) -> float:
    """
    Evaluate a mathematical expression and return the result.

    Args:
        expression: A string containing a mathematical expression

    Returns:
        The numeric result of evaluating the expression

    Raises:
        ValueError: If the expression is invalid or cannot be evaluated
        ZeroDivisionError: If the expression attempts division by zero
    """
    if not expression or not expression.strip():
        raise ValueError("Empty expression")

    try:
        # Using eval with a restricted namespace for safety
        # Only allow basic mathematical operations
        allowed_names = {
            '__builtins__': {}
        }
        result = eval(expression, allowed_names)

        # Ensure the result is numeric
        if not isinstance(result, (int, float)):
            raise ValueError(f"Expression does not evaluate to a number: {type(result).__name__}")

        return float(result)
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")
    except SyntaxError as e:
        raise ValueError(f"Invalid expression syntax: {e}")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
