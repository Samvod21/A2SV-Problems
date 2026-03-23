class Solution(object):
    def findAnagrams(self, s, p):
        n, m = len(s), len(p)
        
        if m > n: 
            return []

        pcount = Counter(p) 
        scount = Counter()
        ans = []
        
        for i in range(n):
            scount[s[i]] += 1

            if i >= m:
                if scount[s[i - m]] == 1:
                    del scount[s[i - m]]
                else:
                    scount[s[i - m]] -= 1

            if scount == pcount:
                ans.append(i - m + 1)

        return ans
            

        