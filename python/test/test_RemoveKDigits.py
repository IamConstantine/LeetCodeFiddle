from unittest import TestCase

from RemoveKDigits import removeKdigits


class Test(TestCase):
    def test_remove_kdigits(self):
        self.assertEqual('0', removeKdigits('10', 1))
        self.assertEqual('1219', removeKdigits('1432219', 3))
