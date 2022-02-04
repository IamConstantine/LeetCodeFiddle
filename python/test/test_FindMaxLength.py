from unittest import TestCase

from FindMaxLength import findMaxLength


class Test(TestCase):
    def test_find_max_length(self):
        self.assertEqual(2, findMaxLength([0,1]))
        self.assertEqual(2, findMaxLength([0,1,0]))
