from unittest import TestCase

from HouseRobber import rob


class Test(TestCase):
    def test_rob(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
        self.assertEqual(12, rob([2, 7, 9, 3, 1]))
        self.assertEqual(3, rob([1,2,1,1]))
