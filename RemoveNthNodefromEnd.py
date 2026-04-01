class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        

        if size == n:
            return head.next
        
        curr = dummy

        for i in range(size - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next