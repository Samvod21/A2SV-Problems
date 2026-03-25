class Solution(object):
    def countGood(self, nums, k):
        dup = 0
        r = 0
        c = Counter()
        l = 0
        n = 0

        while l < len(nums):
            while r < len(nums) and dup < k:
                dup += c[nums[r]]
                c[nums[r]] += 1
                r += 1
            
            if dup >= k:
                n += len(nums) - r + 1
            
            c[nums[l]] -= 1
            dup -= c[nums[l]]
            l += 1
        
        return n
        