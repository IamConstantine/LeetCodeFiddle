from unittest import TestCase

from MakeStringSorted import makeStringSorted


class Test(TestCase):
    def test_make_string_sorted(self):
        self.assertEqual(5, makeStringSorted("cba"))
        self.assertEqual(63, makeStringSorted("cdbea"))
        self.assertEqual(982157772, makeStringSorted("leetcodeleetcodeleetcode"))
