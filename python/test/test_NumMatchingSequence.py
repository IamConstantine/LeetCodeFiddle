from unittest import TestCase

from NumMatchingSequence import numMatchingSubseq


class Test(TestCase):
    def test_num_matching_subseq(self):
        self.assertEqual(3, numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"]))
        self.assertEqual(2, numMatchingSubseq('dsahjpjauf', ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
