from unittest import TestCase

from LargestBSTSubtree import largestBSTSubtree
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_largest_bstsubtree(self):
        self.assertEqual(3, largestBSTSubtree(createBinaryTreeFrom([10, 5, 15, 1, 8, None, 7])))
        self.assertEqual(2, largestBSTSubtree(
            createBinaryTreeFrom([4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1])))
