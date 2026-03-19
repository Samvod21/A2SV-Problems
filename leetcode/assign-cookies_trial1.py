class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        f = 0
        n = 0
        c = 0

        while f < len(g) and n < len(s):
            if g[f] <= s[n]:
                c += 1
                f += 1
                n += 1
            
            else:
                n += 1
        
        return c
        