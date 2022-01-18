from unittest import TestCase

from MonotonicArray import isMonotonic


class Test(TestCase):
    def test_is_monotonic(self):
        self.assertEqual(True, isMonotonic([1, 2, 2, 3]))
        self.assertEqual(True, isMonotonic([6, 5, 4, 4]))
        self.assertEqual(False, isMonotonic([1, 3, 2]))
