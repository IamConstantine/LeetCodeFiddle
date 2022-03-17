from unittest import TestCase

from ScoreOfParantheses import scoreOfParentheses


class Test(TestCase):
    def test_score_of_parentheses(self):
        self.assertEqual(2, scoreOfParentheses('(())'))
        self.assertEqual(4, scoreOfParentheses('(()())'))
        self.assertEqual(8, scoreOfParentheses('(((())))'))
