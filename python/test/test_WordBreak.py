from unittest import TestCase

from WordBreak import wordBreak


class Test(TestCase):
    def test_word_break(self):
        self.assertEqual(True, wordBreak("leetcode", ["leet","code"]))
        self.assertEqual(True, wordBreak("applepenapple", ["apple","pen"]))
        self.assertEqual(False, wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
