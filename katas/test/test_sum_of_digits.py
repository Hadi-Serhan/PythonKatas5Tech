import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits_with_numbers(self):
        self.assertEqual(sum_of_digits("abc123"), 6)  # 1 + 2 + 3 = 6
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)  # 5 + 2 = 7

    def test_sum_of_digits_without_numbers(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)  # No digits, sum should be 0

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)  # Empty string, sum should be 0