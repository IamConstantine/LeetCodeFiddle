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