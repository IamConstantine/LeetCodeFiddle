from unittest import TestCase

from IsSubtree import isSubtree
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_is_subtree(self):
        # self.assertEqual(True, isSubtree(createBinaryTreeFrom([3, 4, 5, 1, 2]), createBinaryTreeFrom([4, 1, 2])))
        self.assertEqual(True, isSubtree(createBinaryTreeFrom([1, 1]), createBinaryTreeFrom([1])))
