from unittest import TestCase

from AlienDictionary import alienOrder


class Test(TestCase):
    def test_alien_order(self):
        self.assertEqual('wertf', alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
        self.assertEqual('zx', alienOrder(["z", "x"]))
        self.assertEqual('', alienOrder(["z", "x", "z"]))
