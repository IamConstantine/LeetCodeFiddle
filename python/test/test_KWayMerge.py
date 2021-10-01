from unittest import TestCase

from KWayMerge import mergeKLists
from ListNode import createListNode, linkedListToList


class Test(TestCase):
    def test_merge_klists(self):
        input = [[1, 4, 5], [1, 3, 4], [2, 6]]
        inputListNodes = [createListNode(x) for x in input]
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], linkedListToList(mergeKLists(inputListNodes)))
