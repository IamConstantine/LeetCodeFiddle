from unittest import TestCase

from WordSearch_ii import findWords


class Test(TestCase):
    def test_find_words(self):
        self.assertEqual(["eat", "oath"], sorted(findWords(
            [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            ["oath", "pea", "eat", "rain"])))
