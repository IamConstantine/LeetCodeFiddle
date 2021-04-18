from unittest import TestCase

from AddTwoNumbers import addTwoNumbers
from ListNode import linkedListToList, createListNode


class Test(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual([7, 0, 8],
                         linkedListToList(addTwoNumbers(createListNode([2, 4, 3]), createListNode([5, 6, 4]))))