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


def mergeKLists(lists):
    # TLE Error.
    if not lists:
        return None
    while len(lists) > 1:
        l1 = lists.pop()
        l2 = lists.pop()
        new_head = mergeTwoLists(l1, l2)
        lists.insert(0, new_head)
    return lists[0]


def mergeKLists2(lists):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = self.mergeKLists(lists[:mid])
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r
