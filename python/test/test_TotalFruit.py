from unittest import TestCase

from TotalFruit import totalFruit


class Test(TestCase):
    def test_total_fruit(self):
        self.assertEquals(3, totalFruit([1,2,1]))
        self.assertEquals(3, totalFruit([0,1,2,2]))
        self.assertEquals(5, totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
        self.assertEquals(3, totalFruit([1,0,1,4,1]))

