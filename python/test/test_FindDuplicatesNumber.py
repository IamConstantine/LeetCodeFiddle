from unittest import TestCase

from FindDuplicatesNumber import findDuplicate


class Test(TestCase):
    def test_find_duplicate(self):
        self.assertEqual(2, findDuplicate([1, 3, 4, 2, 2]))
        self.assertEqual(2, findDuplicate([2, 2, 2, 2, 2]))
        self.assertEqual(3, findDuplicate([3, 1, 3, 4, 2]))
