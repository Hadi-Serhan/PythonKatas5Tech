import unittest
from katas.longest_common_prefix import longest_common_prefix 

class TestLongestCommonPrefix(unittest.TestCase):
    def test_common_prefix_exists(self):
        self.assertEqual(
            longest_common_prefix(["flower", "flow", "flight"]),
            "fl"
        )

    def test_no_common_prefix(self):
        self.assertEqual(
            longest_common_prefix(["dog", "racecar", "car"]),
            ""
        )

    def test_full_word_common_prefix(self):
        self.assertEqual(
            longest_common_prefix(["same", "same", "same"]),
            "same"
        )

    def test_single_string(self):
        self.assertEqual(
            longest_common_prefix(["alone"]),
            "alone"
        )

    def test_empty_list(self):
        self.assertEqual(
            longest_common_prefix([]),
            ""
        )

    def test_common_prefix_partial(self):
        self.assertEqual(
            longest_common_prefix(["apple", "apricot", "ape"]),
            "ap"
        )

    def test_mixed_case(self):
        self.assertEqual(
            longest_common_prefix(["App", "apple", "application"]),
            ""  
        )

    def test_common_prefix_inter(self):
        self.assertEqual(
            longest_common_prefix(["interspecies", "interstellar", "interstate"]),
            "inters"
        )