class Solution(object):
    def validPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                res = self.cheakPalindrom(s, l + 1, r) or self.cheakPalindrom(s, l, r - 1)
                return res
        
            l += 1
            r -= 1
        
        return True

    
    @staticmethod
    def cheakPalindrom(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
                
        