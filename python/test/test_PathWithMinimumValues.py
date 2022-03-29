from unittest import TestCase

from PathWithMinimumValues import maximumMinimumPath


class Test(TestCase):
    def test_maximum_minimum_path(self):
        self.assertEqual(4, maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
        self.assertEqual(2, maximumMinimumPath([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]))
