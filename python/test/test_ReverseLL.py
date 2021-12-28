from unittest import TestCase

from ListNode import createListNode, linkedListToList
from ReverseLL import reverseList


class Test(TestCase):
    def test_reverse_list(self):
        self.assertEqual([5,4,3,2,1], linkedListToList(reverseList(createListNode([1,2,3,4,5]))))
        self.assertEqual([2,1], linkedListToList(reverseList(createListNode([1,2]))))
        self.assertEqual([], linkedListToList(reverseList(createListNode([]))))
