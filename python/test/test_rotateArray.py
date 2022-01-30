from unittest import TestCase

from RotateArray import rotate


class Test(TestCase):
    def test_rotateArray(self):
        testCase1 = [1, 2, 3, 4, 5, 6, 7]
        rotate(testCase1, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], testCase1)
