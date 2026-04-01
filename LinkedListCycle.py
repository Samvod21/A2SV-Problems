class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None