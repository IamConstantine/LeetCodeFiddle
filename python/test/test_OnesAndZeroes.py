from unittest import TestCase

from OnesAndZeroes import findMaxForm


class Test(TestCase):
    def test_find_max_form(self):
        self.assertEqual(4, findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
        self.assertEqual(2, findMaxForm(["10", "0", "1"], 1, 1))
