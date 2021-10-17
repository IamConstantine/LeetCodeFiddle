from unittest import TestCase

from MaximumGenerated import getMaximumGenerated


class Test(TestCase):
    def test_get_maximum_generated(self):
        self.assertEqual(3, getMaximumGenerated(7))
        self.assertEqual(1, getMaximumGenerated(2))
        self.assertEqual(2, getMaximumGenerated(3))
