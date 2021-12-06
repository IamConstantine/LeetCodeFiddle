from unittest import TestCase

from SetZeroes import setZeroes


class Test(TestCase):
    def test_set_zeroes(self):
        input1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        setZeroes(input1)
        self.assertEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]], input1)

        input2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        setZeroes(input2)
        self.assertEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], input2)
