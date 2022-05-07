from unittest import TestCase

from Tree import createBinaryTreeFrom, toTreeArray
from UpsideDownBinaryTree import upsideDownBinaryTree


class Test(TestCase):
    def test_upside_down_binary_tree(self):
        self.assertEqual([4, 5, 2, None, None, 3, 1],
                         toTreeArray(upsideDownBinaryTree(createBinaryTreeFrom([1, 2, 3, 4, 5]))))
        self.assertEqual([1], toTreeArray(upsideDownBinaryTree(createBinaryTreeFrom([1]))))
