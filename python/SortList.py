# https://leetcode.com/problems/sort-list
# Medium
# T = O(NlogN)
# S = O(log N) - for stack
from ListNode import ListNode


def merge(h1, h2):
    if not h1 or not h2:
        return h1 or h2

    if h1.val > h2.val:
        h1, h2 = h2, h1

    head = prev = h1
    h1 = h1.next

    while h1 and h2:
        if h1.val < h2.val:
            prev.next = h1
            h1 = h1.next
        else:
            prev.next = h2
            h2 = h2.next
        prev = prev.next

    prev.next = h1 or h2

    return head


def split_list(head):
    pre, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = None
    return head, slow


def sortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    h1, h2 = split_list(head)
    h1, h2 = sortList(h1), sortList(h2)
    return merge(h1, h2)
