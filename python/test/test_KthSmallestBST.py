from unittest import TestCase

from KthSmallestBST import kthSmallest
from Tree import createBinaryTreeFrom


class Test(TestCase):
    def test_kth_smallest(self):
        self.assertEqual(1, kthSmallest(createBinaryTreeFrom([3, 1, 4, None, 2]), 1))
        self.assertEqual(3, kthSmallest(createBinaryTreeFrom([5,3,6,2,4,None,None,1]), 3))
