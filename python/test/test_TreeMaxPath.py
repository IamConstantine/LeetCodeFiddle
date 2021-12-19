from unittest import TestCase

from Tree import createBinaryTreeFrom
from TreeMaxPath import maxPathSum


class Test(TestCase):
    def test_max_path_sum(self):
        self.assertEqual(42, maxPathSum(createBinaryTreeFrom([-10, 9, 20, None, None, 15, 7])))
        self.assertEqual(6, maxPathSum(createBinaryTreeFrom([1, 2, 3])))
        self.assertEqual(2, maxPathSum(createBinaryTreeFrom([2, -1, -2])))
