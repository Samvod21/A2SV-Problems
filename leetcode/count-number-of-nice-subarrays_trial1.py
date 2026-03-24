class Solution(object):
    def numberOfSubarrays(self, nums, k):
        lastdel = -1
        diff = 0
        odds = []
        subs = 0

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odds.append(i)
            
            if len(odds) > k:
                lastdel = odds.pop()
            
            elif len(odds) == k:
                diff = abs(odds[0] - lastdel)
                subs += diff
        
        return subs

        