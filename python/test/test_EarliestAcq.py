from unittest import TestCase

from EarliestAcq import earliestAcq


class Test(TestCase):
    def test_earliest_acq(self):
        self.assertEqual(20190301, earliestAcq(
            [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
             [20190312, 1, 2], [20190322, 4, 5]], 6))

        self.assertEqual(3, earliestAcq([[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4))
        self.assertEqual(5, earliestAcq([[5,4,3],[2,0,4],[1,1,2],[0,0,2],[9,1,3],[3,1,4],[8,2,4],[6,1,0]], 5))
