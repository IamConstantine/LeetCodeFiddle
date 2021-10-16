import time
from unittest import TestCase

from Tribonacci import tribonacci, tribonacci_dp


class Test(TestCase):
    def test_tribonacci(self):
        self.assertEqual(4, tribonacci(4))

        # time the two approaches
        start = time.time()
        tribonacci(25)
        end = time.time()
        print(round((end - start) * 1000000, 3))

        start = time.time()
        tribonacci_dp(25)
        end = time.time()
        print(round((end - start) * 1000000, 3))


        self.assertEqual(1389537, tribonacci(25))
