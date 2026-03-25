class Solution(object):
    def checkInclusion(self, s1, s2):
        size = len(s1)
        cs1 = Counter(s1)

        for i in range(len(s2) - size + 1):
            win = s2[i: i + size]

            if Counter(win) == cs1:
                return True
        
        return False
        