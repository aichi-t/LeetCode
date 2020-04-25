class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    head = ListNode(0)
    current_node = head
    while l1 and l2:
        if l1.val <= l2.val:
            current_node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            current_node.next = ListNode(l2.val)
            l2 = l2.next
        current_node = current_node.next
    if l1:
        current_node.next = l1
    else:
        current_node.next = l2

    return head.next

    def mergeTwoLists2(l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    n3 = ListNode(4)
    n2 = ListNode(2)
    n1 = ListNode(1)
    n6 = ListNode(4)
    n5 = ListNode(3)
    n4 = ListNode(1)

    n2.next = n3
    n1.next = n2
    n5.next = n6
    n4.next = n5
    mergeTwoLists(n1, n4)
