from unittest import TestCase

from NextPermutation import nextPermutation


class Test(TestCase):
    def test_next_permutation(self):
        l = [1, 2, 3]
        nextPermutation(l)
        self.assertEqual([1, 3, 2], l)

        l = [1, 1, 5]
        nextPermutation(l)
        self.assertEqual([1, 5, 1], l)

        l = [3, 2, 1]
        nextPermutation(l)
        self.assertEqual([1, 2, 3], l)
