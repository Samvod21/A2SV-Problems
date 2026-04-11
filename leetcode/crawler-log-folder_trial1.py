class Solution(object):
    def minOperations(self, logs):
        stack = []

        for s in logs:
            if s != "../":
                if s != "./":
                    stack.append(s)
            
            else:
                if len(stack) > 0:
                    stack.pop()
        
        return len(stack)
        