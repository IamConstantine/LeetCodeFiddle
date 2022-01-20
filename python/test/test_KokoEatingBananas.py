from unittest import TestCase

from KokoEatingBananas import minEatingSpeed


class Test(TestCase):
    def test_min_eating_speed(self):
        self.assertEqual(4, minEatingSpeed([3, 6, 7, 11], 8))
        self.assertEqual(30, minEatingSpeed([30, 11, 23, 4, 20], 5))
        self.assertEqual(23, minEatingSpeed([30, 11, 23, 4, 20], 6))
