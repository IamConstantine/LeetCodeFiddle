from unittest import TestCase

from ValidTree import validTree


class Test(TestCase):
    def test_valid_tree(self):
        self.assertEqual(True, validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertEqual(False, validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
