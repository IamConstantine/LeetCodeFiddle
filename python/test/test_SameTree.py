from unittest import TestCase

from SameTree import isSameTree
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_is_same_tree(self):
        self.assertEqual(False, isSameTree(createBinaryTreeFrom([0, -5]), createBinaryTreeFrom([0, -8])))
        # self.assertEqual(True, isSameTree(createBinaryTreeFrom([1, 2, 3]), createBinaryTreeFrom([1, 2, 3])))
        # self.assertEqual(False, isSameTree(createBinaryTreeFrom([1, 2]), createBinaryTreeFrom([1, None, 2])))
        # self.assertEqual(False, isSameTree(createBinaryTreeFrom([1, 2, 1]), createBinaryTreeFrom([1, 1, 2])))
