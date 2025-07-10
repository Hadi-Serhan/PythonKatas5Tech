import unittest
from katas.list_flatten import flatten_list

class TestFlattenList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_integer(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_flat_list(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_nested_list(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_complex_nested_list(self):
        self.assertEqual(flatten_list([[1], [2, [3]], [[4]]]), [1, 2, 3, 4])