from unittest import TestCase

from MaxDepthTree import maxDepth
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_max_depth(self):
        self.assertEqual(3, maxDepth(createBinaryTreeFrom([3, 9, 20, None, None, 15, 7])))
        self.assertEqual(2, maxDepth(createBinaryTreeFrom([1, None, 2])))
