from unittest import TestCase

from Strobogrammatic import isStrobogrammatic


class Test(TestCase):
    def test_is_strobogrammatic(self):
        self.assertEqual(True, isStrobogrammatic("69"))
        self.assertEqual(True, isStrobogrammatic("1"))
        self.assertEqual(False, isStrobogrammatic("2"))
        self.assertEqual(False, isStrobogrammatic("962"))
