from unittest import TestCase

from PascalTriangle import generate


class Test(TestCase):
    def test_generate(self):
        self.assertEqual([[1]], generate(1))
        self.assertEqual([[1], [1, 1]], generate(2))
        self.assertEqual([[1], [1, 1], [1, 2, 1]], generate(3))
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], generate(5))
