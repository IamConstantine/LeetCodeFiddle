from unittest import TestCase

from WinnerSquareGames import winnerSquareGame


class Test(TestCase):
    def test_winner_square_game(self):
        self.assertEqual(True, winnerSquareGame(1))
        self.assertEqual(False, winnerSquareGame(2))
        self.assertEqual(True, winnerSquareGame(4))
