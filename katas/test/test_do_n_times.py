from io import StringIO
import unittest
from unittest.mock import Mock, patch
from katas.do_n_times import do_n_times, say_hello, print_message

class TestDoNTimes(unittest.TestCase):
    def test_function_called_correct_number_of_times(self):
        """Test if the function is called the correct number of times."""
        mock_func = Mock()
        do_n_times(mock_func, 3)
        self.assertEqual(mock_func.call_count, 3)
        
    def test_zero_times(self):
        """Test if the function is not called when n is 0."""
        mock_func = Mock()
        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 0)
        
    def test_negative_times(self):
        """Test if the function is not called when n is negative."""
        mock_func = Mock()
        do_n_times(mock_func, -5)
        self.assertEqual(mock_func.call_count, 0)
        
    def test_say_hello(self):
        expected_output = "Hello!\n" * 3
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            do_n_times(say_hello, 3)
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
    def test_print_message(self):
        expected_output = "Python is fun!\n" * 5
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            do_n_times(print_message, 5)
            self.assertEqual(mock_stdout.getvalue(), expected_output)