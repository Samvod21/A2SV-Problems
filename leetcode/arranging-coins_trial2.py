class Solution(object):
    def arrangeCoins(self, n):
        l = 1
        r= n

        while l <= r:
            mid = l + (r - l) // 2
            total = mid * (mid + 1) // 2
            
            if total == n:
                return mid
            
            elif total < n:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return r
        
        

        