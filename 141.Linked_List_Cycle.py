class Solution:
    def hasCycle(self,head):
        # slow = fast = head
        # while fast != None and fast.next != None:
        #     slow = slow.next
        #     fast =  fast.next.next
        #     if slow == fast:
        #         return True
        # return False
        try:
            slow = fast = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
