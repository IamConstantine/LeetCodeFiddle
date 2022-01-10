from unittest import TestCase

from NonOverlappingIntervals import eraseOverlapIntervals


class Test(TestCase):
    def test_erase_overlap_intervals(self):
        self.assertEqual(1, eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
        self.assertEqual(2, eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
        self.assertEqual(0, eraseOverlapIntervals([[1, 2], [2, 3]]))
