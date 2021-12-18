from unittest import TestCase

from ValidPalindrome import isPalindrome


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(True, isPalindrome(" "))
        self.assertEqual(False, isPalindrome("race a car"))
