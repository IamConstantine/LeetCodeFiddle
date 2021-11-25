from unittest import TestCase

from CountVowelStrings import countVowelStrings


class Test(TestCase):
    def test_count_vowel_strings(self):
        self.assertEqual(5, countVowelStrings(1))
        self.assertEqual(15, countVowelStrings(2))
        self.assertEqual(66045, countVowelStrings(33))
