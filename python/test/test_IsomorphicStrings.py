from unittest import TestCase

from IsomorphicStrings import isIsomorphic


class Test(TestCase):
    def test_is_isomorphic(self):
        self.assertEqual(True, isIsomorphic('egg', 'add'))
        self.assertEqual(True, isIsomorphic('paper', 'title'))
        self.assertEqual(False, isIsomorphic('foo', 'bar'))
        self.assertEqual(False, isIsomorphic('badc', 'baba'))
