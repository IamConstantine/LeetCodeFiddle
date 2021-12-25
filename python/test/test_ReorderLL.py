from unittest import TestCase

from ListNode import createListNode, linkedListToList
from ReorderLL import reorderList


class Test(TestCase):
    def test_reorder_list(self):
        head = createListNode([1, 2, 3, 4])
        reorderList(head)
        self.assertEqual([1, 4, 2, 3], linkedListToList(head))

        head = createListNode([1, 2, 3, 4, 5])
        reorderList(head)
        self.assertEqual([1, 5, 2, 4, 3], linkedListToList(head))
