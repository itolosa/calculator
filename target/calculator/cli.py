"""Calculator CLI module.

This module provides the command-line interface for the calculator.
"""

import sys

from calculator.parser import parse


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
    print("Calculator REPL. Type 'exit' or 'quit' to exit.")
    while True:
        try:
            expression = input(">> ")
            if expression.lower() in ('exit', 'quit'):
                break
            if not expression.strip():
                continue
            result = parse(expression)
            print(result)
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            break
    return 0
