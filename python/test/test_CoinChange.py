from unittest import TestCase

from CoinChange import coinChange


class Test(TestCase):
    def test_coin_change(self):
        self.assertEqual(3, coinChange([1, 2, 5], 11))
        self.assertEqual(-1, coinChange([2], 3))
        self.assertEqual(0, coinChange([1], 0))
        self.assertEqual(20, coinChange([186, 419, 83, 408], 6249))
