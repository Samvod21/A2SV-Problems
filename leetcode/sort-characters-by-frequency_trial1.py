class Solution(object):
    def frequencySort(self, s):
        c = Counter(s)
        
        return "".join(sorted(s, key=lambda x: (-c[x], x)))



        



        