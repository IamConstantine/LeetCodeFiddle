from unittest import TestCase

from ThreeSum import threeSum


class Test(TestCase):
    def test_three_sum(self):
        self.assertEqual([[-2,0,2],[-2,1,1]], threeSum([-2,0,1,1,2]))
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], threeSum([-1,0,1,2,-1,-4]))
        self.assertEqual([[0,0,0]], threeSum([0, 0, 0, 0]))

