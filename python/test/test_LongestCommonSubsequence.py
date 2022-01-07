from unittest import TestCase

from LongestCommonSubsequence import longestCommonSubsequence


class Test(TestCase):
    def test_longest_common_subsequence(self):
        self.assertEqual(3, longestCommonSubsequence('abcde', 'ace'))
        self.assertEqual(3, longestCommonSubsequence('abc', 'abc'))
        self.assertEqual(0, longestCommonSubsequence('abc', 'def'))
