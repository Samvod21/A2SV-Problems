class Solution(object):
    def removeStars(self, s):
        stack = []
        ans = ""

        for c in s:
            if c != '*':
                stack.append(c)
            
            else:
                stack.pop()
        
        for i in stack:
            ans += i
        
        return ans
        
        
        