class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        halfs = self.myPow(x, n // 2)

        if n % 2 == 0:
            return halfs * halfs
        
        return halfs * halfs * x
        