from unittest import TestCase

from MinProductSumOfArray import minProductSum


class Test(TestCase):
    def test_min_product_sum(self):
        self.assertEqual(40, minProductSum([5, 3, 4, 2], [4, 2, 2, 5]))
        self.assertEqual(65, minProductSum([2, 1, 4, 5, 7], [3, 2, 4, 8, 6]))
