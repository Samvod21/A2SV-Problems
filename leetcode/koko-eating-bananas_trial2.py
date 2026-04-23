class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            total = 0
            mid = l + (r - l) // 2
            
            for i in piles:
                total += (i + mid - 1) // mid
            
            if total <= h:
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res




        