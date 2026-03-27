class Solution(object):
    def judgeSquareSum(self, c):
        l = 0

        while l * l <= c:
            r = (c - l * l) ** 0.5
    
            if r == int(r):
                return True
            
            l += 1
        
        return False
        