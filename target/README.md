# Calculator

A simple Python calculator application for basic arithmetic operations.

## Features

- Basic arithmetic operations
- Command-line interface
- Extensible parser for mathematical expressions

## Requirements

- Python >= 3.11

## Installation

```bash
pip install -e .
```

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Run the calculator:

```bash
python -m calculator
```

## Testing

Run tests with pytest:

```bash
pytest
```

## Linting and Formatting

This project uses ruff for linting and formatting:

```bash
# Check code
ruff check .

# Format code
ruff format .
```

## Project Structure

```
calculator/
  __init__.py       - Package initialization
  __main__.py       - Entry point for module execution
  operations.py     - Arithmetic operations
  parser.py         - Expression parser
  cli.py            - Command-line interface
tests/
  __init__.py       - Test package initialization
  test_operations.py - Tests for operations
  test_parser.py    - Tests for parser
  test_cli.py       - Tests for CLI
```

## License

MIT
