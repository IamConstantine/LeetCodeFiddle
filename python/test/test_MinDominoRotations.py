from unittest import TestCase

from MinDominoRotations import minDominoRotations


class Test(TestCase):
    def test_min_domino_rotations(self):
        self.assertEqual(2, minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
        self.assertEqual(-1, minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
