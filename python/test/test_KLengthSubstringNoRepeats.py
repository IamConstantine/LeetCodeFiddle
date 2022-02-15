from unittest import TestCase

from KLengthSubstringNoRepeats import numKLenSubstrNoRepeats


class Test(TestCase):
    def test_num_klen_substr_no_repeats(self):
        self.assertEqual(6, numKLenSubstrNoRepeats('havefunonleetcode', 5))
        self.assertEqual(0, numKLenSubstrNoRepeats('havefunonleetcode', 5))
