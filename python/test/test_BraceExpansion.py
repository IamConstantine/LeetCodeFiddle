from unittest import TestCase

from BraceExpansion import expand


class Test(TestCase):
    def test_expand(self):
        self.assertEqual(["acdf", "acef", "bcdf", "bcef"], expand('{a,b}c{d,e}f'))
        self.assertEqual(['ax', 'ay', 'az', 'bx', 'by', 'bz'], expand('{a,b}{z,x,y}'))
