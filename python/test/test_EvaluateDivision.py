from unittest import TestCase

from EvaluateDivision import calcEquation


class TestSolution(TestCase):
    def test_calc_equation(self):
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
                         calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                      [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000],
                         calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                                      [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
