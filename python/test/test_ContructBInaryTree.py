from unittest import TestCase

from ContructBinaryTree import buildTree
from Tree import toTreeArray


class Test(TestCase):
    def test_build_tree(self):
        self.assertEqual([3, 9, 20, None, None, 15, 7], toTreeArray(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
        self.assertEqual([-1], toTreeArray(buildTree([-1], [-1])))
