# Calculator CLI Usage

A simple command-line calculator with both interactive and non-interactive modes.

## Installation

No installation required. Just ensure you have Python 3.6 or later.

## Usage

### Non-Interactive Mode

Evaluate a single expression:

```bash
python -m calculator "2 + 3"
```

Examples:
```bash
python -m calculator "2 + 3"          # Output: 5.0
python -m calculator "10 / 2 * 3"     # Output: 15.0
python -m calculator "(5 + 3) * 2"    # Output: 16.0
```

Exit codes:
- `0`: Success
- `1`: Error (invalid expression, division by zero, etc.)

### Interactive Mode (REPL)

Start the REPL by running without arguments:

```bash
python -m calculator
```

In the REPL:
- Type mathematical expressions and press Enter to evaluate
- Type `help` to see help text
- Type `exit` or `quit` to exit
- Press Ctrl+D (EOF) or Ctrl+C to exit

Example session:
```
> 2 + 3
5.0
> 10 / 2 * 3
15.0
> (5 + 3) * 2
16.0
> help
Calculator CLI
...
> exit
```

## Supported Operations

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Parentheses: `(` `)`
- Negative numbers: `-5`
- Floating point: `2.5 + 3.5`

## Error Handling

Errors are printed to stderr:
- Invalid syntax
- Division by zero
- Invalid expressions

In interactive mode, errors don't terminate the REPL.
In non-interactive mode, errors cause exit with code 1.

## Running Tests

Run the test suite:

```bash
python run_tests.py
```

Or run specific test modules:

```bash
python -m unittest tests.test_cli
python -m unittest tests.test_evaluator
```
