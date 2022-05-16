from unittest import TestCase

from LargestAndCombination import largestCombination


class Test(TestCase):
    def test_largest_combination(self):
        self.assertEqual(4, largestCombination([16, 17, 71, 62, 12, 24, 14]))
        self.assertEqual(2, largestCombination([8, 8]))
