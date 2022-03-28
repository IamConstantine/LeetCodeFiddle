from unittest import TestCase

from SearchRotatedArray_ii import search


class Test(TestCase):
    def test_search(self):
        self.assertTrue(search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertFalse(search([2, 5, 6, 0, 0, 1, 2], 3))
        self.assertTrue(search([1, 0, 1, 1, 1], 0))
