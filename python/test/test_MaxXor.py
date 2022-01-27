from unittest import TestCase

from MaxXor import findMaximumXOR


class Test(TestCase):
    def test_find_maximum_xor(self):
        self.assertEqual(28, findMaximumXOR([3, 10, 5, 25, 2, 8]))
        self.assertEqual(127, findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
