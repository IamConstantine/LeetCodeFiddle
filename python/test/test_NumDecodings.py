from unittest import TestCase

from NumDecodings import numDecodings


class Test(TestCase):
    def test_num_decodings(self):
        self.assertEqual(2, numDecodings("12"))
        self.assertEqual(3, numDecodings("226"))
        self.assertEqual(0, numDecodings("0"))
        self.assertEqual(0, numDecodings("06"))
        self.assertEqual(1, numDecodings("101"))
        self.assertEqual(2, numDecodings("1331"))

