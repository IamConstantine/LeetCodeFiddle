from unittest import TestCase

from LongestConsecutiveSequence import longestConsecutive


class Test(TestCase):
    def test_longest_consecutive(self):
        self.assertEqual(4, longestConsecutive([100, 4, 200, 1, 3, 2]))
        self.assertEqual(9, longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        self.assertEqual(2, longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8]))
        self.assertEqual(0, longestConsecutive([]))
        self.assertEqual(2, longestConsecutive([0,-1]))
