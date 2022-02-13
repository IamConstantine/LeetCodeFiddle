from unittest import TestCase

from Subsets import subsets


class Test(TestCase):
    def test_subsets(self):
        self.assertCountEqual([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], subsets([1, 2, 3]))
