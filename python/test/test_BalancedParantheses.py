from unittest import TestCase

from BalancedParantheses import isValid


class Test(TestCase):
    def test_is_valid(self):
        self.assertEqual(True, isValid('({})'))
        self.assertEqual(False, isValid('([)]'))
        self.assertEqual(True, isValid('()[]{}'))
