from unittest import TestCase

from PascalTriangle2 import getRow


class Test(TestCase):
    def test_get_row(self):
        self.assertEqual([1,3,3,1], getRow(3))
        self.assertEqual([1], getRow(0))
        self.assertEqual([1,1], getRow(1))
        self.assertEqual([1, 4, 6, 4, 1], getRow(4))
