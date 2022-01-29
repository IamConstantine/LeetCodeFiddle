from unittest import TestCase

from WordSearchII import findWords


class Test(TestCase):
    def test_find_words(self):
        self.assertCountEqual(["eat", "oath"], findWords(
            [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            ["oath", "pea", "eat", "rain"]))

        self.assertEqual([], findWords([["a", "b"], ["c", "d"]], ["abcb"]))
        self.assertEqual(['a'], findWords([["a"]], ["a"]))
