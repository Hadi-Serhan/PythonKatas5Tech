import unittest
from katas.list_diff import find_difference

class TestListDiff(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(find_difference([5]), 0)

    def test_two_elements_list(self):
        self.assertEqual(find_difference([3, 7]), 4)

    def test_multiple_elements_list(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_negative_numbers(self):
        self.assertEqual(find_difference([-10, -3, -5, -6, -20, -2]), 18)