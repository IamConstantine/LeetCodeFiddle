from unittest import TestCase

from LengthOfLongestSubstring import lengthOfLongestSubstring


class Test(TestCase):
    def test_length_of_longest_substring(self):
        self.assertEquals(3, lengthOfLongestSubstring('abcabcbb'))
        self.assertEquals(3, lengthOfLongestSubstring('pwwkew'))
