import heapq
from typing import List

from ListNode import ListNode


def mergeKLists(lists: List[ListNode]) -> ListNode:
    h = [(l.val, idx) for idx, l in enumerate(lists) if l]
    heapq.heapify(h)
    head = cur = ListNode(None)
    while h:
        val, idx = heapq.heappop(h)
        cur.next = ListNode(val)
        cur = cur.next
        node = lists[idx] = lists[idx].next
        if node:
            heapq.heappush(h, (node.val, idx))
    return head.next
