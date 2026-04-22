class Solution(object):
    def countGoodNumbers(self, n):
        lim = 10 ** 9 + 7
        even = (n + 1) // 2
        odd = n // 2

        return self.mul(5, even, lim) * self.mul(4, odd, lim) % lim
    
    def mul(self, x, y, lim):
        res = 1
        pro = x

        while y > 0:
            if y % 2 == 1:
                res = res * pro % lim
            
            pro = pro * pro % lim
            y //= 2
        
        return res
        
        