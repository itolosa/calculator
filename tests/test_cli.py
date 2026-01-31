"""Tests for the calculator CLI."""

import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock
from calculator.cli import run_repl, run_non_interactive, print_help, main


class TestCLI(unittest.TestCase):
    """Test cases for the CLI functions."""

    def test_print_help(self):
        """Test that help text is printed to stdout."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print_help()
            output = fake_stdout.getvalue()
            self.assertIn("Calculator CLI", output)
            self.assertIn("Interactive mode", output)
            self.assertIn("help", output)
            self.assertIn("exit", output)
            self.assertIn("quit", output)

    def test_run_non_interactive_success(self):
        """Test non-interactive mode with valid expression."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            exit_code = run_non_interactive("2 + 3")
            output = fake_stdout.getvalue()
            self.assertEqual(exit_code, 0)
            self.assertEqual(output.strip(), "5.0")

    def test_run_non_interactive_error(self):
        """Test non-interactive mode with invalid expression."""
        with patch('sys.stderr', new=StringIO()) as fake_stderr:
            exit_code = run_non_interactive("2 +")
            error_output = fake_stderr.getvalue()
            self.assertEqual(exit_code, 1)
            self.assertIn("Error:", error_output)

    def test_run_non_interactive_division_by_zero(self):
        """Test non-interactive mode with division by zero."""
        with patch('sys.stderr', new=StringIO()) as fake_stderr:
            exit_code = run_non_interactive("10 / 0")
            error_output = fake_stderr.getvalue()
            self.assertEqual(exit_code, 1)
            self.assertIn("Error:", error_output)
            self.assertIn("zero", error_output.lower())

    @patch('builtins.input')
    def test_repl_simple_expression(self, mock_input):
        """Test REPL with a simple expression."""
        mock_input.side_effect = ["2 + 3", "exit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("5.0", output)

    @patch('builtins.input')
    def test_repl_multiple_expressions(self, mock_input):
        """Test REPL with multiple expressions."""
        mock_input.side_effect = ["2 + 3", "10 / 2", "quit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("5.0", output)
            self.assertIn("5.0", output)

    @patch('builtins.input')
    def test_repl_help_command(self, mock_input):
        """Test REPL help command."""
        mock_input.side_effect = ["help", "exit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("Calculator CLI", output)

    @patch('builtins.input')
    def test_repl_error_handling(self, mock_input):
        """Test REPL error handling."""
        mock_input.side_effect = ["2 +", "2 + 3", "exit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            with patch('sys.stderr', new=StringIO()) as fake_stderr:
                run_repl()
                stdout = fake_stdout.getvalue()
                stderr = fake_stderr.getvalue()
                # Error should be printed to stderr
                self.assertIn("Error:", stderr)
                # Valid expression result should be in stdout
                self.assertIn("5.0", stdout)

    @patch('builtins.input')
    def test_repl_empty_input(self, mock_input):
        """Test REPL with empty input."""
        mock_input.side_effect = ["", "2 + 3", "exit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            # Should skip empty input and evaluate the next expression
            self.assertIn("5.0", output)

    @patch('builtins.input')
    def test_repl_eof(self, mock_input):
        """Test REPL handling of EOF (Ctrl+D)."""
        mock_input.side_effect = EOFError()
        with patch('sys.stdout', new=StringIO()):
            # Should exit gracefully without raising exception
            run_repl()

    @patch('builtins.input')
    def test_repl_keyboard_interrupt(self, mock_input):
        """Test REPL handling of KeyboardInterrupt (Ctrl+C)."""
        mock_input.side_effect = KeyboardInterrupt()
        with patch('sys.stdout', new=StringIO()):
            # Should exit gracefully without raising exception
            run_repl()

    @patch('builtins.input')
    def test_repl_quit_command(self, mock_input):
        """Test REPL quit command."""
        mock_input.side_effect = ["2 + 3", "quit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("5.0", output)

    @patch('builtins.input')
    def test_repl_exit_command(self, mock_input):
        """Test REPL exit command."""
        mock_input.side_effect = ["2 + 3", "exit"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("5.0", output)

    @patch('builtins.input')
    def test_repl_case_insensitive_commands(self, mock_input):
        """Test that special commands are case-insensitive."""
        mock_input.side_effect = ["HELP", "EXIT"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            run_repl()
            output = fake_stdout.getvalue()
            self.assertIn("Calculator CLI", output)

    def test_main_with_arguments(self):
        """Test main function with command-line arguments."""
        test_args = ['calculator', '2 + 3']
        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                with self.assertRaises(SystemExit) as cm:
                    main()
                self.assertEqual(cm.exception.code, 0)
                output = fake_stdout.getvalue()
                self.assertEqual(output.strip(), "5.0")

    def test_main_with_error(self):
        """Test main function with invalid expression."""
        test_args = ['calculator', '2 +']
        with patch.object(sys, 'argv', test_args):
            with patch('sys.stderr', new=StringIO()) as fake_stderr:
                with self.assertRaises(SystemExit) as cm:
                    main()
                self.assertEqual(cm.exception.code, 1)
                error = fake_stderr.getvalue()
                self.assertIn("Error:", error)

    @patch('builtins.input')
    def test_main_without_arguments(self, mock_input):
        """Test main function without arguments (REPL mode)."""
        test_args = ['calculator']
        mock_input.side_effect = ["2 + 3", "exit"]
        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                main()
                output = fake_stdout.getvalue()
                self.assertIn("5.0", output)


if __name__ == '__main__':
    unittest.main()
