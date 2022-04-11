from unittest import TestCase

from MinimizeResultUsingParanthesis import minimizeResult


class Test(TestCase):
    def test_minimize_result(self):
        self.assertEqual('2(47+38)', minimizeResult('247+38'))
        self.assertEqual('1(2+3)4', minimizeResult('12+34'))
