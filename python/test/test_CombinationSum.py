from unittest import TestCase
import time

from CombinationSum import combinationSum


class Test(TestCase):
    def test_combination_sum(self):
        self.assertEqual([], combinationSum([2], 1))
        self.assertEqual([[2, 2, 3], [7]], combinationSum([2, 3, 6, 7], 7))
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], combinationSum([2, 3, 5], 8))

        # time in microseconds
        start = time.time()
        for iterations in range(10):
            combinationSum([2, 3, 6, 7], 7)
        end = time.time()
        print(round((end - start) * 1000000, 3))