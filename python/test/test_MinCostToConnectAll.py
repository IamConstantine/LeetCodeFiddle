from unittest import TestCase

from MinCostToConnectAll import PrimsOptimized


class TestKruskal(TestCase):
    def test_min_cost_connect_points(self):
        obj = PrimsOptimized()
        self.assertEqual(20, obj.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
        self.assertEqual(18, obj.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
