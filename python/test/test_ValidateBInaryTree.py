from unittest import TestCase

from Tree import createBinaryTreeFrom
from ValidateBinaryTree import isValidBST, isValidBSTPreorder


class Test(TestCase):
    def test_is_valid_bst(self):
        self.assertEqual(True, isValidBSTPreorder(createBinaryTreeFrom([2, 1, 3])))
        self.assertEqual(False, isValidBSTPreorder(createBinaryTreeFrom([5, 1, 4, None, None, 3, 6])))
        self.assertEqual(False, isValidBSTPreorder(createBinaryTreeFrom([120,70,140,50,100,130,160,20,55,75,110,119,135,150,200])))
        self.assertEqual(False, isValidBSTPreorder(createBinaryTreeFrom([5,4,6,None,None,3,7])))
        self.assertEqual(False, isValidBSTPreorder(createBinaryTreeFrom([5, 14, None, 1])))
        self.assertEqual(True, isValidBSTPreorder(createBinaryTreeFrom([0, -1])))
        self.assertEqual(False, isValidBSTPreorder(createBinaryTreeFrom([2,2,2])))
