from unittest import TestCase

from HouseRobberII import rob_ii


class Test(TestCase):
    def test_rob_ii(self):
        self.assertEqual(3, rob_ii([2, 3, 2]))
        self.assertEqual(4, rob_ii([1, 2, 3, 1]))
        self.assertEqual(3, rob_ii([1, 2, 3]))
