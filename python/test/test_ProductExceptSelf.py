from unittest import TestCase

from ProductExceptSelf import productExceptSelf


class Test(TestCase):
    def test_product_except_self(self):
        self.assertEqual([24, 12, 8, 6], productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([0, 0, 9, 0, 0], productExceptSelf([-1, 1, 0, -3, 3]))
