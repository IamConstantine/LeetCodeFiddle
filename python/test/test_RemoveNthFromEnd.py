from unittest import TestCase

from ListNode import createListNode, linkedListToList
from RemoveNthFromEnd import removeNthFromEnd


class Test(TestCase):
    def test_remove_nth_from_end(self):
        self.assertEqual([1, 2, 3, 5], linkedListToList(removeNthFromEnd(createListNode([1, 2, 3, 4, 5]), 2)))
        self.assertEqual([], linkedListToList(removeNthFromEnd(createListNode([1]), 1)))
