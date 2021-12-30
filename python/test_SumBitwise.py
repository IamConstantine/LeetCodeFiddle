from unittest import TestCase

from SumBitwise import getSum


class Test(TestCase):
    def test_get_sum(self):
        self.assertEqual(8, getSum(3, 5))
        self.assertEqual(0, getSum(-1, 1))
