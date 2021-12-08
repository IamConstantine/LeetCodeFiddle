from unittest import TestCase

from WordSearch import exist


class Test(TestCase):
    def test_exist(self):
        self.assertEqual(True, exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
        self.assertEqual(True, exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'SEE'))
        self.assertEqual(False, exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCB'))
