from unittest import TestCase

from Fibonacci import fib


class Test(TestCase):
    def test_fib(self):
        self.assertEqual(1, fib(2))
        self.assertEqual(3, fib(4))
