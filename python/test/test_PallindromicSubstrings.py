from unittest import TestCase

from PallindromicSubstrings import countSubstrings


class Test(TestCase):
    def test_count_substrings(self):
        self.assertEqual(3, countSubstrings('abc'))
        self.assertEqual(6, countSubstrings('aaa'))
