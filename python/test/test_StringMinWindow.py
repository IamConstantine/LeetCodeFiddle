from unittest import TestCase

from StringMinWindow import minWindow, minWindowWithFilteredS, minWindowLessComplex


class Test(TestCase):
    def test_min_window(self):
        self.assertEqual('BANC', minWindow('ADOBECODEBANC', 'ABC'))
        self.assertEqual('A', minWindow('A', 'A'))
        self.assertEqual('', minWindow('A', 'AA'))

        self.assertEqual('BANC', minWindowWithFilteredS('ADOBECODEBANC', 'ABC'))
        self.assertEqual('A', minWindowWithFilteredS('A', 'A'))
        self.assertEqual('', minWindowWithFilteredS('A', 'AA'))

        self.assertEqual('BANC', minWindowLessComplex('ADOBECODEBANC', 'ABC'))
        self.assertEqual('A', minWindowLessComplex('A', 'A'))
        self.assertEqual('', minWindowLessComplex('A', 'AA'))
