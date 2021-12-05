from unittest import TestCase

from InsertIntervals import insert


class Test(TestCase):
    def test_insert(self):
        self.assertEqual([[1, 5], [6, 9]], insert([[1, 3], [6, 9]], [2, 5]))
        self.assertEqual([[1, 2], [3, 10], [12, 16]], insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
        self.assertEqual([[5, 7]], insert([], [5, 7]))
        self.assertEqual([[1, 5]], insert([[1,5]], [2,3]))
        self.assertEqual([[1, 7]], insert([[1,5]], [2,7]))
