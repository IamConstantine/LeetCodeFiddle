from ListNode import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
