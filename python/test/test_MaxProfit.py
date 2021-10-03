from unittest import TestCase

from MaxProfit import maxProfit


class Test(TestCase):
    def test_max_profit(self):
        self.assertEqual(5, maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, maxProfit([7, 6, 4, 3, 1]))
