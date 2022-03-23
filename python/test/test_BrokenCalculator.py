from unittest import TestCase

from BrokenCalculator import brokenCalc


class Test(TestCase):
    def test_broken_calc(self):
        self.assertEqual(2, brokenCalc(2, 3))
        self.assertEqual(3, brokenCalc(3, 10))
        self.assertEqual(2, brokenCalc(5, 8))
