from unittest import TestCase

from LengthOfLIS import lengthOfLIS


class Test(TestCase):
    def test_length_of_lis(self):
        self.assertEqual(4, lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, lengthOfLIS([0, 1, 0, 3, 2, 3]))
        self.assertEqual(1, lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual(3, lengthOfLIS([4,10,4,3,8,9]))
