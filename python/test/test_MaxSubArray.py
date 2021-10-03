from unittest import TestCase

from MaxSubArray import maxSubArray


class Test(TestCase):
    def test_max_sub_array(self):
        self.assertEqual(6, maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, maxSubArray([1]))
        self.assertEqual(23, maxSubArray([5, 4, -1, 7, 8]))
