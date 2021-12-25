from typing import Optional

from ListNode import ListNode


# https://leetcode.com/problems/linked-list-cycle
# Easy
# T = O(N) - p to get to cycle and k for two pointers to meet
# S = O(1)

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    # Detecting start of loop
    # slow = head
    # while slow != fast:
    #     slow = slow.next
    #     fast = fast.next

    return False
