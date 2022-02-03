from unittest import TestCase

from FourSum import fourSumCount


class Test(TestCase):
    def test_four_sum_count(self):
        self.assertEqual(2, fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
        self.assertEqual(6, fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
