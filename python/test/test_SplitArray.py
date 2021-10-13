from unittest import TestCase

from SplitArray import splitArray


class Test(TestCase):
    def test_split_array(self):
        self.assertEqual(18, splitArray([7, 2, 5, 10, 8], 2))
        self.assertEqual(9, splitArray([1, 2, 3, 4, 5], 2))
        self.assertEqual(4, splitArray([1, 4, 4], 3))
