"""Main entry point for the calculator module.

This module allows the calculator to be run as: python -m calculator
"""

import sys

from calculator.cli import main

if __name__ == "__main__":
    sys.exit(main())
