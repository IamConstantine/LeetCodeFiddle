from unittest import TestCase

from Tree import createBinaryTreeFrom
from WidthOfTree import widthOfBinaryTree


class Test(TestCase):
    def test_width_of_binary_tree(self):
        self.assertEqual(4, widthOfBinaryTree(createBinaryTreeFrom([1, 3, 2, 5, 3, None, 9])))
        self.assertEqual(2, widthOfBinaryTree(createBinaryTreeFrom([1, 3, None, 5, 3])))
