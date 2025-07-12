import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)

    def test_multiple_words(self):
        self.assertEqual(count_words("This is a test"), 4)

    def test_punctuation(self):
        self.assertEqual(count_words("Hello, world! This is a test."), 6)

    def test_numbers_and_letters(self):
        self.assertEqual(count_words("Test123 and 456test"), 3)

    def test_mixed_characters(self):
        self.assertEqual(count_words("Hello! How are you?"), 4)
        
    def test_leading_trailing_spaces(self):
        self.assertEqual(count_words(" ,  Leading and trailing spaces   "), 4)