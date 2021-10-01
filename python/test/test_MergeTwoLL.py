from unittest import TestCase

from ListNode import createListNode, linkedListToList
from MergeTwoLL import mergeTwoLists


class Test(TestCase):
    def test_merge_two_lists(self):
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         linkedListToList(mergeTwoLists(createListNode([1, 2, 4]), createListNode([1, 3, 4]))))

        self.assertEqual([],
                         linkedListToList(mergeTwoLists(createListNode([]), createListNode([]))))
