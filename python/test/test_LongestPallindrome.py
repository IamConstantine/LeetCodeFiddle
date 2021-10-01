from unittest import TestCase

from LongestPallindrome import longestPalindrome


class Test(TestCase):
    def test_longest_palindrome(self):
        self.assertEqual("bab", longestPalindrome("babad"))
