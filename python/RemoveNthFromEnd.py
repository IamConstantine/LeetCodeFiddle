from ListNode import ListNode


def removeNthFromEndTwoPass(head: ListNode, n: int) -> ListNode:
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next

    result = ListNode(0, head)
    ptr = 0
    temp = result
    while temp and ptr < length - n:
        ptr += 1
        temp = temp.next
    temp.next = temp.next.next
    return result.next


# solve using 0th and nth ptr
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    first = head
    while n:
        n -= 1
        first = first.next

    result = ListNode(0, head)
    second = result
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return result.next
