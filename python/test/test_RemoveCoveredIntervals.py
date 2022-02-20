from unittest import TestCase

from RemoveCoveredIntervals import removeCoveredIntervals


class Test(TestCase):
    def test_remove_covered_intervals(self):
        self.assertEqual(2, removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
        self.assertEqual(1, removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
