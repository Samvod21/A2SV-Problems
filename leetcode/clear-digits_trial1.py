class Solution(object):
    def clearDigits(self, s):
        stack = []

        for i in s:
            if i >= 'a' and i <= 'z':
                stack.append(i)
            
            else:
                if len(stack) > 0:
                    stack.pop()
        
        if len(stack) == 0:
            return ""
        
        return "".join(stack)
        