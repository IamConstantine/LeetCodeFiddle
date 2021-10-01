from unittest import TestCase

from RotateImage import rotate


class Test(TestCase):
    def test_rotate(self):
        testCase1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(testCase1)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], testCase1)

        testCase2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        rotate(testCase2)
        self.assertEqual([[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], testCase2)
