from unittest import TestCase

from IsSubsequence import isSubsequence


class Test(TestCase):
    def test_is_subsequence(self):
        self.assertEqual(True, isSubsequence('abc', 'ahbgdc'))
        self.assertEqual(False, isSubsequence('axc', 'ahbgdc'))



