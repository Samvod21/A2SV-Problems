class Solution(object):
    def kthGrammar(self, n, k):
        if n <= 1:
            return 0
        
        total = 1

        for _ in range(n - 1):
            total *= 2
        
        half = total / 2

        if k > half:
            return 1 - self.kthGrammar(n, k - half)
        
        else:
            return self.kthGrammar(n - 1, k)
        