from unittest import TestCase

from SpiralOrder import spiralOrder


class Test(TestCase):
    def test_spiral_order(self):
        self.assertEqual([3, 2], spiralOrder([[3], [2]]))
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], spiralOrder(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
