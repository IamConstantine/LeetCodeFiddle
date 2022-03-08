from unittest import TestCase

from Strobogrammatic_ii import findStrobogrammatic


class Test(TestCase):
    def test_find_strobogrammatic(self):
        self.assertEqual(["11", "69", "88", "96"], findStrobogrammatic(2))
        self.assertEqual(["0", "1", "8"], findStrobogrammatic(1))
