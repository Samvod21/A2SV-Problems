class Solution(object):
    def restoreString(self, s, indices):
        pairs = []
        res = []
        st = ""

        for i, j in zip(s, indices):
            pairs.append([i, j])
        

        for i in range(0, len(s)):
            for j, k in pairs:
                if i == k:
                    res.append(j)
        
        
        for i in res:
            st += i
        
        return st
# 2 13