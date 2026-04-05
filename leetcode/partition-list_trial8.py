# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        lesshead = ListNode(0)
        greathead = ListNode(0)
        less = lesshead
        great = greathead
        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = curr
            
            else:
                great.next = curr
                great = curr
            
            curr = curr.next
        
        great.next = None
        less.next = greathead.next
        

        
        return lesshead.next

        

        