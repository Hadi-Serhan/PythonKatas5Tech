import unittest
from katas.is_unique_str import is_unique
class TestIsUniqueStr(unittest.TestCase):
    def test_is_unique_str(self):
        self.assertFalse(is_unique("Hello"))  # 'l' is repeated
        self.assertTrue(is_unique("World"))   # all characters are unique
        self.assertTrue(is_unique("Python"))  # all characters are unique
        self.assertTrue(is_unique("Unique"))   # all characters are unique
        self.assertTrue(is_unique(""))  # empty string should return True
        self.assertFalse(is_unique(" ab "))
        