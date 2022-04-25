from unittest import TestCase

from CountLaticePoints import countLatticePoints


class Test(TestCase):
    def test_count_lattice_points(self):
        self.assertEqual(5, countLatticePoints([[2, 2, 1]]))
        self.assertEqual(16, countLatticePoints([[2, 2, 2], [3, 4, 1]]))
