class Solution(object):
    def shipWithinDays(self, weights, days):
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            
            if self.check(weights, mid, days):
                r = mid - 1
            
            else:
                l = mid + 1
        
        return l
    
    def check(self, weights, mid, days):
        total = 0
        day = 1

        for i in weights:
            if total + i > mid:
                day += 1
                total = i
            
            else:
                total += i
        
        return day <= days


        