from unittest import TestCase

from CountSetBits import hammingWeight


class Test(TestCase):
    def test_hamming_weight(self):
        self.assertEqual(3, hammingWeight(int('00000000000000000000000000001011', 2)))
        self.assertEqual(1, hammingWeight(int('00000000000000000000000010000000', 2)))
