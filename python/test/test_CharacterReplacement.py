from unittest import TestCase

from CharacterReplacement import characterReplacement


class Test(TestCase):
    def test_character_replacement(self):
        self.assertEqual(4, characterReplacement('ABAB', 2))
        self.assertEqual(4, characterReplacement('AABABBA', 1))
