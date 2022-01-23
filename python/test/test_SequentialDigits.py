from unittest import TestCase

from SequentialDigits import sequentialDigits


class Test(TestCase):
    def test_sequential_digits(self):
        self.assertEqual([123, 234], sequentialDigits(100, 300))
