from unittest import TestCase

from LadderLength import ladderLength


class Test(TestCase):
    def test_ladder_length(self):
        self.assertEqual(5, ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
        self.assertEqual(0, ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
