# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        node = ListNode(0)
        node.next = head
        curr = node

        while curr.next and curr.next.next:
            f = curr.next
            s = curr.next.next
            f.next = s.next
            s.next = f
            curr.next = s
            curr = f
        
        return node.next

        