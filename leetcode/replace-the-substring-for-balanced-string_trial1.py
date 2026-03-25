class Solution(object):
    def balancedString(self, s):
        n = len(s)
        c = Counter(s)
        minimum = len(s)
        target = "QWER"
        l = 0
        
        if all(c[i] <= n // 4 for i in target):
            return 0
        
        for r in range(len(s)):
            c[s[r]] -= 1

            while l < len(s) and all(c[i] <= n // 4 for i in target):
                minimum = min(minimum, r -l + 1)
                c[s[l]] += 1
                l += 1
        
        return minimum
                
            

                
        