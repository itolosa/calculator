"""Calculator CLI module.

This module provides the command-line interface for the calculator.
"""

import sys

from calculator.parser import parse

HELP_TEXT = """Calculator CLI - Help

Usage:
  Interactive mode (REPL):
    > <expression>         Evaluate a mathematical expression
    > help                 Show this help message
    > exit                 Exit the calculator
    > quit                 Exit the calculator

  Non-interactive mode:
    python -m calculator "expression"

Supported operations:
  + (addition), - (subtraction), * (multiplication), / (division)
  Parentheses for grouping: ( )

Examples:
  > 2 + 3
  5.0
  > (10 - 2) * 4
  32.0
  > 15 / 3
  5.0
"""


def main(args=None):
    """Main entry point for the calculator CLI.

    Args:
        args: Command-line arguments. If None, uses sys.argv.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0:
        return repl()
    else:
        expression = ' '.join(args)
        try:
            result = parse(expression)
            print(result)
            return 0
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


def repl():
    """Run the Read-Eval-Print Loop.

    Returns:
        Exit code (always 0).
    """
    while True:
        try:
            expression = input("> ")

            if expression.lower() in ('exit', 'quit'):
                break

            if expression.lower() == 'help':
                print(HELP_TEXT)
                continue

            if not expression.strip():
                continue

            result = parse(expression)
            print(result)
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}", file=sys.stderr)
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            break
    return 0
