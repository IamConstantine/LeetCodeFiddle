from unittest import TestCase

from PlusOne import plusOne


class Test(TestCase):
    def test_plus_one(self):
        self.assertEqual([1, 2, 4], plusOne([1, 2, 3]))
        self.assertEqual([1, 0, 0, 0], plusOne([9, 9, 9]))
        self.assertEqual([1, 1, 0, 0], plusOne([1, 0, 9, 9]))
        self.assertEqual([1], plusOne([0]))
