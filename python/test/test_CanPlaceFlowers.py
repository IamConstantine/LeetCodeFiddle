from unittest import TestCase

from CanPlaceFlowers import canPlaceFlowers


class Test(TestCase):
    def test_can_place_flowers(self):
        self.assertEqual(True, canPlaceFlowers([0, 0, 1], 1))
        self.assertEqual(True, canPlaceFlowers([0], 1))
        self.assertEqual(True, canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertEqual(False, canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertEqual(False, canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
