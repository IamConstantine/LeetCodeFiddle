from unittest import TestCase

from CampusBikes import assignBikes


class Test(TestCase):
    def test_assign_bikes(self):
        self.assertEqual([0, 2, 1], assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))
