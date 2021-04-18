from ListNode import ListNode


def addTwoNumbers(l1: ListNode, l2: ListNode):
    carry = 0
    sum = ListNode(0)
    prev = sum

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        carry, mod = divmod(val1 + val2 + carry, 10)
        curr = ListNode(mod)
        prev.next = curr
        prev = curr
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        prev.next = ListNode(1)
    return sum.next
