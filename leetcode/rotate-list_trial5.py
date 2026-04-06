# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        c = 1
        dummy = head

        while dummy.next:
            #prev = prev.next
            dummy = dummy.next
            c += 1
        
        pos = k % c

        if pos == 0:
            return head
        
        curr = head

        for _ in range(c - pos - 1):
            curr = curr.next
        
        head1 = curr.next
        curr.next = None
        dummy.next = head
        
        return head1
        

            
            
        
        return head

            

        