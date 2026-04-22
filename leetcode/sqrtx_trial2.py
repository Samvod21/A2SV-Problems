class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
            
        l = 0
        r = x // 2

        while l <= r:
            mid = (l + r) // 2
            res = mid * mid

            if res == x:
                return mid
            
            elif res > x:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return r
        