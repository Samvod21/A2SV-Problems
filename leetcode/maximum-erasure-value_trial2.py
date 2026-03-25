class Solution(object):
    def maximumUniqueSubarray(self, nums):
        dup = set()
        s = 0
        maxsum = 0
        l = 0
        
        for r in range(len(nums)):
            while nums[r] in dup:
                dup.remove(nums[l])
                s -= nums[l]
                l += 1
            
            s += nums[r]
            dup.add(nums[r])
            maxsum = max(maxsum, s)
        
        return maxsum
