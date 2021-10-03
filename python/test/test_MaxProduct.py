from unittest import TestCase

from MaxProduct import maxProduct


class Test(TestCase):
    def test_max_product(self):
        # self.assertEqual(6, maxProduct([2, 3, -2, 4]))
        # self.assertEqual(0, maxProduct([-2, 0, -1]))
        self.assertEqual(24, maxProduct([-2, -3, 2, -4]))
        self.assertEqual(48, maxProduct([-2, -3, -2, -4]))
