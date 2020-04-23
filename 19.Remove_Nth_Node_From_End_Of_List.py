class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthNodeFromEnd(head, n):
    # One Pass? Solution
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def removeNthNodeFromEnd2(head, n):
    # Two Pass solution
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    node = head
    while node != None:
        length += 1
        node = node.next
    length -= n
    node = dummy
    while length > 0:
        length -= 1
        node = node.next
    node.next = node.next.next
    return dummy.next


def removeNthNodeFromEnd3(head, n):
    """
    Interesting solution from the discussions.
    Instead of removing the Nth node, remove the nth value by shifting all nodes that are larger than N.
    """
    def index(node):
        if not node:
            return 0
        i = index(node.next) + 1
        if i > n:
            node.next.val = node.val
        return i
    index(head)
    return head
