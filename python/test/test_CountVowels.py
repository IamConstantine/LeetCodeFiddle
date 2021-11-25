from unittest import TestCase

from CountVowels import countVowels, countVowels_dp


class Test(TestCase):
    def test_count_vowels(self):
        self.assertEqual(6, countVowels("kbk"))
        self.assertEqual(3, countVowels("kbc"))
        self.assertEqual(0, countVowels("ltcd"))
        self.assertEqual(237, countVowels("bnnskbksbnnsk"))
