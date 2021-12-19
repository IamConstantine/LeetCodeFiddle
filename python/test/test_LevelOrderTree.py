from unittest import TestCase

from LevelOrderTree import levelOrder
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_level_order(self):
        self.assertEqual([[3],[9,20],[15,7]], levelOrder(createBinaryTreeFrom([3,9,20,None,None,15,7])))
        self.assertEqual([[1]], levelOrder(createBinaryTreeFrom([1])))
        self.assertEqual([], levelOrder(createBinaryTreeFrom([])))
