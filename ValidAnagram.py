from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        
        diction1 = Counter(s)
        diction2 = Counter(t)

        for key1, val1 in diction1.items():
            for key2, val2 in diction2.items():
                if key1 == key2 and val1 != val2:
                    return False
        
        s1 = set(s)
        t1 = set(t)

        if t1.issubset(s1):
            return True
        
        return False
# 2 11