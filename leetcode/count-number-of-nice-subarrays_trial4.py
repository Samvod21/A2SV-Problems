class Solution(object):
    def numberOfSubarrays(self, nums, k):
        lastdel = -1
        diff = 0
        odds = []
        subs = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odds.append(i)
            
                if len(odds) > k:
                    lastdel = odds.pop(0)
                
                if len(odds) == k:
                    diff = odds[0] - lastdel
            
            if len(odds) == k:
                subs += diff
        
        return subs

        