from unittest import TestCase

from MergeIntervals import merge


class Test(TestCase):
    def test_merge(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], merge([[1, 3], [2, 6], [15, 18], [8, 10]]))
        self.assertEqual([[1,5]], merge([[1, 4], [4, 5]]))
        self.assertEqual([[1,4]], merge([[1,4],[2,3]]))
