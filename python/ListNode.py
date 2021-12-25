class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def createListNode(elements):
    if not elements:
        return None
    head = prev = ListNode(elements[0])
    for val in elements[1:]:
        curr = ListNode(val)
        prev.next = curr
        prev = curr
    return head


def createLL_with_cycle(arr, pos):
    if not arr:
        return None
    head = createListNode(arr)
    curr = head
    cycle_head = head
    i = 0
    while curr.next:
        if i == pos:
            cycle_head = curr
        i += 1
        curr = curr.next
    if pos != -1:
        curr.next = cycle_head
    return head
