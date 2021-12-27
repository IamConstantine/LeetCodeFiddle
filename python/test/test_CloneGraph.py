from unittest import TestCase

from CloneGraph import buildNodeGraph, buildAdjacencyList, cloneGraph


class Test(TestCase):
    def test_clone_graph(self):
        self.assertEqual([[2, 4], [1, 3], [2, 4], [1, 3]],
                         buildAdjacencyList(cloneGraph(buildNodeGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))))

        self.assertEqual([],
                         buildAdjacencyList(cloneGraph(buildNodeGraph([]))))
