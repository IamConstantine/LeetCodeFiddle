from unittest import TestCase

from ClimbStairs import climbStairs


class Test(TestCase):
    def test_climb_stairs(self):
        self.assertEqual(3, climbStairs(3))
        self.assertEqual(2, climbStairs(2))
