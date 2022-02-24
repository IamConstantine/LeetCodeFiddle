from unittest import TestCase

from ListNode import createListNode, linkedListToList
from SortList import sortList


class Test(TestCase):
    def test_sort_list(self):
        self.assertEqual([1,2,3,4], linkedListToList(sortList(createListNode([4, 2, 1, 3]))))
