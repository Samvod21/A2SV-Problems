"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head

        dic = {None: None}
        curr = head

        while curr:
            node = Node(curr.val)
            dic[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            dup = dic[curr]
            dup.next = dic[curr.next]
            dup.random = dic[curr.random]
            curr = curr.next
        
        return dic[head]
        