from unittest import TestCase

from ShortestPathLength import shortestPathLength


class Test(TestCase):
    def test_shortest_path_length(self):
        self.assertEqual(4, shortestPathLength([[1, 2, 3], [0], [0], [0]]))
        self.assertEqual(4, shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
