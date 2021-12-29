from unittest import TestCase

from IsAnagram import isAnagram


class Test(TestCase):
    def test_is_anagram(self):
        self.assertEqual(True, isAnagram('anagram', 'nagaram'))
        self.assertEqual(False, isAnagram('rat', 'car'))
        self.assertEqual(False, isAnagram('aacc', 'ccac'))
