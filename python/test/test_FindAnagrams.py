from unittest import TestCase

from FindAnagrams import findAnagrams


class Test(TestCase):
    def test_find_anagrams(self):
        self.assertEqual([0, 6], findAnagrams('cbaebabacd', 'abc'))
        self.assertEqual([0, 1, 2], findAnagrams('abab', 'ab'))
