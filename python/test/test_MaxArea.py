from unittest import TestCase

from MaxArea import maxArea


class Test(TestCase):
    def test_max_area(self):
        self.assertEqual(49, maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(16, maxArea([4,3,2,1,4]))
        self.assertEqual(2, maxArea([1,2,1]))
