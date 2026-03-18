class Solution(object):
    def appendCharacters(self, s, t):
        start = 0
        exists = 0

        while start < len(s) and exists < len(t):
            if s[start] == t[exists]:
                exists += 1
            
            start += 1
        
        res = len(t) - exists

        return res
        