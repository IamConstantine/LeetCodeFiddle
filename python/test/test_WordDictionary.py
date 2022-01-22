from unittest import TestCase

from WordDictionary import WordDictionary


class TestWordDictionary(TestCase):
    def test_search(self):
        obj = WordDictionary()
        obj.addWord('bad')
        obj.addWord('dad')
        obj.addWord('mad')
        self.assertTrue(obj.search('bad'))
        self.assertFalse(obj.search('pad'))
        self.assertFalse(obj.search('ad'))
        self.assertFalse(obj.search('ba'))
