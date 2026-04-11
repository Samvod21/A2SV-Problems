class Solution(object):
    def firstUniqChar(self, s):
        fre = {}

        for ch in s:
            fre[ch] = fre.get(ch, 0) + 1
        
        for i, c in enumerate(s):
            if fre[c] == 1:
                return i
        
        return -1
        
        
        
                
        
