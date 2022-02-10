from unittest import TestCase

from SubArraySum import subarraySum


class Test(TestCase):
    def test_subarray_sum(self):
        self.assertEqual(2, subarraySum([1, 1, 1], 2))
        self.assertEqual(2, subarraySum([1, 2, 3], 3))
        self.assertEqual(4, subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))
