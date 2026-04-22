"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        
        curr = head
        childs = []

        while curr:
            if curr.child:
                if curr.next:
                    childs.append(curr.next)
            
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None

            elif childs and not curr.next:
                node = childs.pop()
                curr.next = node
                node.prev = curr
            
            curr = curr.next
        
        return head

        