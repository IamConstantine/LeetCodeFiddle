import time
from unittest import TestCase

from groupAnagrams import groupAnagrams, groupAnagramsBest


class Test(TestCase):
    def test_group_anagrams(self):
        self.assertEqual([[""]], groupAnagrams([""]))
        self.assertEqual([["a"]], groupAnagrams(["a"]))

        # depending on the hash function used in the dict, this order might change.
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        # time in microseconds
        start = time.time()
        for iterations in range(10):
            groupAnagramsBest(["eat","tea","tan","ate","nat","bat"])
        end = time.time()
        print(round((end - start) * 1000000, 3))
