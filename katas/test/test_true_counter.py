import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_count_true_values(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)  # 3 True values
        self.assertEqual(count_true_values([False, False, False]), 0)  # No True values
        self.assertEqual(count_true_values([True, True, True]), 3)  # All True values
        self.assertEqual(count_true_values([]), 0)  # Empty list