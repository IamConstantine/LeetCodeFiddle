from unittest import TestCase

from GasStation import canCompleteCircuit


class Test(TestCase):
    def test_can_complete_circuit(self):
        self.assertEqual(3, canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        self.assertEqual(-1, canCompleteCircuit([2, 3, 4], [3, 4, 3]))
