from unittest import TestCase

from SmallestStringWithSwaps import smallestStringWithSwaps


class Test(TestCase):
    def test_smallest_string_with_swaps(self):
        self.assertEqual('bacd', smallestStringWithSwaps('dcab', [[0, 3], [1, 2]]))
        self.assertEqual('abcd', smallestStringWithSwaps('dcab', [[0, 3], [1, 2], [0, 2]]))
        self.assertEqual('abc', smallestStringWithSwaps('cba',  [[0,1],[1,2]]))
