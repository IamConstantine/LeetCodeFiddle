from unittest import TestCase

from Tree import invertTree, createBinaryTreeFrom, levelOrder


class TestSolution(TestCase):
    def test_InvertTree(self):
        # root = createBinaryTreeFrom([4, 2, 7, 1, 3, 6, 9])
        # self.assertEquals([4,7,2,9,6,3,1], bfs(invertTree(root)))

        root = createBinaryTreeFrom([1 ,2])
        self.assertEquals([1, None, 2], invertTree(root))

    # def test_createBinaryTree(self):
        # bin_tree_array = [4, 2, 7, 1, 3, 6, 9]
        # self.assertEquals([4, 2, 7, 1, 3, 6, 9], levelOrder(createBinaryTreeFrom(bin_tree_array)))

        # bin_tree_array = [1, None, 2]
        # self.assertEquals([1, None, 2], levelOrder(createBinaryTreeFrom(bin_tree_array)))
