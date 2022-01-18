from unittest import TestCase

from MaxDistToClosest import maxDistToClosest


class Test(TestCase):
    def test_max_dist_to_closest(self):
        self.assertEqual(3, maxDistToClosest([1, 0, 0, 0]))
        self.assertEqual(2, maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
        self.assertEqual(1, maxDistToClosest([0, 1]))
