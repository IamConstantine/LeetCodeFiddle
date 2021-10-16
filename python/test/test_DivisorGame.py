from unittest import TestCase

from DivisorGame import divisorGame


class Test(TestCase):
    def test_divisor_game(self):
        self.assertEqual(False, divisorGame(1))
        self.assertEqual(True, divisorGame(2))
        self.assertEqual(False, divisorGame(3))
        self.assertEqual(True, divisorGame(4))

