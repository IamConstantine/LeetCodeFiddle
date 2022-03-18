from unittest import TestCase

from RemoveDuplicateLetters import removeDuplicateLetters


class Test(TestCase):
    def test_remove_duplicate_letters(self):
        self.assertEqual('abc', removeDuplicateLetters('bcabc'))
        self.assertEqual('acdb', removeDuplicateLetters('cbacdcbc'))
