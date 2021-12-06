from unittest import TestCase

from UniquePaths import uniquePaths, uniquePathsRecur


class Test(TestCase):
    def test_unique_paths(self):
        self.assertEqual(3, uniquePathsRecur(3, 2))
        self.assertEqual(28, uniquePathsRecur(3, 7))
