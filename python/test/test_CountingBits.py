from unittest import TestCase

from CountingBits import countBits


class Test(TestCase):
    def test_count_bits(self):
        self.assertEqual([0, 1, 1], countBits(2))
        self.assertEqual([0, 1, 1, 2, 1, 2], countBits(5))
