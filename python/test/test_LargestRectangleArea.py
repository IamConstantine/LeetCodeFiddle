from unittest import TestCase

from LargestRectangleArea import largestRectangleArea


class Test(TestCase):
    def test_largest_rectangle_area(self):
        # self.assertEqual(4, largestRectangleArea([2, 4]))
        self.assertEqual(10, largestRectangleArea([2, 1, 5, 6, 2, 3]))
