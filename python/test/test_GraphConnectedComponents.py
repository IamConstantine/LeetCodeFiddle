from unittest import TestCase

from GraphConnectedComponents import countComponents


class Test(TestCase):
    def test_count_components(self):
        self.assertEqual(2, countComponents(5, [[0, 1], [1, 2], [3, 4]]))
        self.assertEqual(1, countComponents(3, [[2, 0], [2, 1]]))
        self.assertEqual(3, countComponents(10, [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [7, 8], [4, 9]]))
        self.assertEqual(2, countComponents(5, [[0, 1], [1, 2], [0, 2], [3, 4]]))
