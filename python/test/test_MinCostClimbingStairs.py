import time
from unittest import TestCase

from MinCostClimbingStairs import minCostClimbingStairs, minCostClimbingStairs_bottom_up, \
    minCostClimbingStairs_withConstantSpace


class Test(TestCase):
    def test_min_cost_climbing_stairs(self):
        self.assertEqual(15, minCostClimbingStairs([10, 15, 20]))

        # time the two approaches
        start = time.time()
        minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        end = time.time()
        print(round((end - start) * 1000000, 3))

        start = time.time()
        minCostClimbingStairs_bottom_up([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        end = time.time()
        print(round((end - start) * 1000000, 3))

        start = time.time()
        minCostClimbingStairs_withConstantSpace([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        end = time.time()
        print(round((end - start) * 1000000, 3))

        self.assertEqual(6, minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
