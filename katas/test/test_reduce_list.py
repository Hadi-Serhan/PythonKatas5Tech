import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(reduce_array([]))

    def test_single_element(self):
        self.assertEqual(reduce_array([5]), [5])

    def test_multiple_elements(self):
        self.assertEqual(reduce_array([10, 15, 7, 20, 25]), [10, 5, -8, 13, 5])
        self.assertEqual(reduce_array([1, 2, 3]), [1, 1, 1])
        self.assertEqual(reduce_array([5, 3, 8]), [5, -2, 5])
        
    def test_negative_numbers(self):
        self.assertEqual(reduce_array([-5, -3, -8]), [-5, 2, -5])
        self.assertEqual(reduce_array([-10, -15, -7]), [-10, -5, 8])
        
    def test_mixed_numbers(self):
        self.assertEqual(reduce_array([10, -5, 15]), [10, -15, 20])
        self.assertEqual(reduce_array([-1, 0, 1]), [-1, 1, 1])