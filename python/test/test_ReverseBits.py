from unittest import TestCase

from ReverseBits import reverseBits


class Test(TestCase):
    def test_reverse_bits(self):
        self.assertEqual(964176192, reverseBits(int('00000010100101000001111010011100', 2)))
        self.assertEqual(3221225471, reverseBits(int('11111111111111111111111111111101', 2)))
