"""Tests for calculator CLI module."""

from io import StringIO
from unittest import mock

from calculator.cli import main, repl


class TestNonInteractiveMode:
    """Tests for non-interactive mode."""

    def test_simple_expression_success(self):
        """Test that simple expression returns correct result."""
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(['2', '+', '3'])
            assert result == 0
            assert mock_stdout.getvalue().strip() == '5.0'

    def test_complex_expression_success(self):
        """Test that complex expression returns correct result."""
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(['(2', '+', '3)', '*', '4'])
            assert result == 0
            assert mock_stdout.getvalue().strip() == '20.0'

    def test_division_success(self):
        """Test that division expression returns correct result."""
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(['10', '/', '2'])
            assert result == 0
            assert mock_stdout.getvalue().strip() == '5.0'

    def test_syntax_error_returns_1(self):
        """Test that syntax error returns exit code 1."""
        with mock.patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            result = main(['2', '+', '+', '3'])
            assert result == 1
            assert 'Error:' in mock_stderr.getvalue()

    def test_division_by_zero_returns_1(self):
        """Test that division by zero returns exit code 1."""
        with mock.patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            result = main(['5', '/', '0'])
            assert result == 1
            assert 'Error:' in mock_stderr.getvalue()

    def test_empty_expression_returns_1(self):
        """Test that empty expression returns exit code 1."""
        with mock.patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            result = main([''])
            assert result == 1
            assert 'Error:' in mock_stderr.getvalue()


class TestREPLMode:
    """Tests for REPL mode."""

    def test_repl_simple_calculation(self):
        """Test that REPL processes simple calculation."""
        with mock.patch('builtins.input', side_effect=['2 + 3', 'exit']):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = repl()
                assert result == 0
                output = mock_stdout.getvalue()
                assert '5.0' in output

    def test_repl_multiple_calculations(self):
        """Test that REPL processes multiple calculations."""
        with mock.patch('builtins.input', side_effect=['2 + 3', '10 - 4', 'quit']):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = repl()
                assert result == 0
                output = mock_stdout.getvalue()
                assert '5.0' in output
                assert '6.0' in output

    def test_repl_error_handling(self):
        """Test that REPL handles errors gracefully."""
        with mock.patch('builtins.input', side_effect=['2 + + 3', 'exit']):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = repl()
                assert result == 0
                output = mock_stdout.getvalue()
                assert 'Error:' in output

    def test_repl_division_by_zero(self):
        """Test that REPL handles division by zero."""
        with mock.patch('builtins.input', side_effect=['5 / 0', 'exit']):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = repl()
                assert result == 0
                output = mock_stdout.getvalue()
                assert 'Error:' in output

    def test_repl_empty_input(self):
        """Test that REPL handles empty input."""
        with mock.patch('builtins.input', side_effect=['', '2 + 2', 'exit']):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = repl()
                assert result == 0
                output = mock_stdout.getvalue()
                assert '4.0' in output

    def test_repl_eof(self):
        """Test that REPL handles EOF."""
        with mock.patch('builtins.input', side_effect=EOFError):
            with mock.patch('sys.stdout', new_callable=StringIO):
                result = repl()
                assert result == 0

    def test_repl_keyboard_interrupt(self):
        """Test that REPL handles keyboard interrupt."""
        with mock.patch('builtins.input', side_effect=KeyboardInterrupt):
            with mock.patch('sys.stdout', new_callable=StringIO):
                result = repl()
                assert result == 0

    def test_repl_exit_command(self):
        """Test that REPL exits with 'exit' command."""
        with mock.patch('builtins.input', side_effect=['exit']):
            with mock.patch('sys.stdout', new_callable=StringIO):
                result = repl()
                assert result == 0

    def test_repl_quit_command(self):
        """Test that REPL exits with 'quit' command."""
        with mock.patch('builtins.input', side_effect=['quit']):
            with mock.patch('sys.stdout', new_callable=StringIO):
                result = repl()
                assert result == 0


class TestMainWithNoArgs:
    """Tests for main with no arguments."""

    def test_main_no_args_calls_repl(self):
        """Test that main with no args calls repl."""
        with mock.patch('calculator.cli.repl', return_value=0) as mock_repl:
            result = main([])
            assert result == 0
            mock_repl.assert_called_once()
