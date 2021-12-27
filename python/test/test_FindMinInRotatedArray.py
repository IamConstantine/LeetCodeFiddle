from unittest import TestCase

from FindMinInRotatedArray import findMin


class Test(TestCase):
    def test_find_min(self):
        self.assertEqual(1, findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(11, findMin([11, 13, 15, 17]))
        self.assertEqual(1, findMin([3,1,2]))
