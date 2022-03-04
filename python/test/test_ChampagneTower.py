from unittest import TestCase

from ChampagneTower import champagneTower


class Test(TestCase):
    def test_champagne_tower(self):
        self.assertEqual(0, champagneTower(1, 1, 1))
        self.assertEqual(1, champagneTower(100000009, 33, 17))
