from typing import Optional

from ListNode import ListNode


# https://leetcode.com/problems/reverse-linked-list
# Easy
# T = O(N)
# S = O(1) - modified the current LL

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev
