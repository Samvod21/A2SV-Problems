# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        s = 0
        c = 0

        while l1 or l2 or c:
            s = c

            if l1:
                s += l1.val
                l1 = l1.next
            
            if l2:
                s += l2.val
                l2 = l2.next
            
            num = s % 10
            c = s // 10
            node = ListNode(num)
            dummy.next = node
            dummy = dummy.next
        
        return curr.next
        