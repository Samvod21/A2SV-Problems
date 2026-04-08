# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        size = 0
        curr = head
        ans = []

        while curr:
            size += 1
            curr = curr.next
        
        groups = size // k
        extra = size % k
        curr = head

        for i in range(k):
            if i < extra:
                subsize = groups + 1
            else:
                subsize = groups
            
            if subsize != 0:
                subhead = curr

                for _ in range(subsize - 1):
                    curr = curr.next

                node = curr.next
                curr.next = None
                ans.append(subhead)
                curr = node
            
            else:
                ans.append(None)
                
        return ans

            


        