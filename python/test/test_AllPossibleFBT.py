from unittest import TestCase

from AllPossibleFBT import allPossibleFBT
from Tree import levelOrder, toTreeArray


class Test(TestCase):
    def test_all_possible_fbt(self):
        self.assertEqual([[0, 0, 0]], [toTreeArray(x) for x in allPossibleFBT(3)])
        self.assertEqual([[0, 0, 0, None, None, 0, 0], [0, 0, 0, 0, 0]], [toTreeArray(x) for x in allPossibleFBT(5)])

        self.assertEqual(
            [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, None, None, None, None, 0, 0], [0, 0, 0, 0, 0, None, None, 0, 0]], [toTreeArray(x) for x in allPossibleFBT(7)])
