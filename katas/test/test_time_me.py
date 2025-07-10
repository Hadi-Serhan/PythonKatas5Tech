import unittest
from katas.time_me import measure_execution_time, sample_function, quick_function
class TestTimeMe(unittest.TestCase):
    def test_measure_execution_time_sample_function(self):
        time_taken = measure_execution_time(sample_function)
        self.assertGreaterEqual(time_taken, 0.5)  # Should be at least 500ms
        self.assertLess(time_taken, 1.0)  # Should be less than 1 second

    def test_measure_execution_time_quick_function(self):
        time_taken = measure_execution_time(quick_function)
        self.assertLess(time_taken, 0.1)  # Should be less than 100ms
        