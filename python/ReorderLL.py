from typing import Optional

from ListNode import ListNode


# https://leetcode.com/problems/reorder-list
# Medium
# T = O(N) S = O(N) - additional list. But can be done inplace by
# splitting the list using slow, fast ptrs, revere second part and then both

def reorderList(head: Optional[ListNode]) -> None:
    curr = head
    l = []
    while curr:
        l.append(curr)
        curr = curr.next

    i = 0
    j = len(l) - 1
    while i <= j:
        if i == j:
            l[i].next = None
            i += 1
        else:
            first = l[i]
            last = l[j]
            first.next = last
            i += 1
            j -= 1
            last.next = l[i] if i <= j else None


# S = O(1)
# LC runtime was slower than my solution

def reorderList(head: ListNode) -> None:
    if not head:
        return

        # find the middle of linked list [Problem 876]
    # in 1->2->3->4->5->6 find 4
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # reverse the second part of the list [Problem 206]
    # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
    # reverse the second half in-place
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists [Problem 21]
    # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
