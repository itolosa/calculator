"""Command-line interface for the calculator."""

import sys
from .evaluator import evaluate


HELP_TEXT = """Calculator CLI

Interactive mode:
  Type mathematical expressions and press Enter to evaluate them.
  Special commands:
    help  - Show this help message
    exit  - Exit the calculator
    quit  - Exit the calculator

Non-interactive mode:
  python -m calculator "expression"

Examples:
  > 2 + 3
  5.0
  > 10 / 2 * 3
  15.0
  > (5 + 3) * 2
  16.0
"""


def print_help():
    """Print the help text to stdout."""
    print(HELP_TEXT)


def run_repl():
    """
    Run the calculator in interactive REPL mode.

    Prints a prompt, waits for user input, evaluates expressions,
    and prints results. Special commands 'help', 'exit', and 'quit'
    are supported.
    """
    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ('exit', 'quit'):
                break

            if user_input.lower() == 'help':
                print_help()
                continue

            result = evaluate(user_input)
            print(result)

        except EOFError:
            # Handle Ctrl+D gracefully
            print()
            break
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print()
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}", file=sys.stderr)


def run_non_interactive(expression: str) -> int:
    """
    Run the calculator in non-interactive mode.

    Evaluates a single expression and prints the result to stdout.
    If an error occurs, prints the error to stderr and returns exit code 1.

    Args:
        expression: The mathematical expression to evaluate

    Returns:
        Exit code: 0 on success, 1 on error
    """
    try:
        result = evaluate(expression)
        print(result)
        return 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main():
    """
    Main entry point for the CLI.

    If command-line arguments are provided, runs in non-interactive mode.
    Otherwise, starts the REPL.
    """
    if len(sys.argv) > 1:
        # Non-interactive mode
        expression = sys.argv[1]
        exit_code = run_non_interactive(expression)
        sys.exit(exit_code)
    else:
        # Interactive mode (REPL)
        run_repl()


if __name__ == '__main__':
    main()
