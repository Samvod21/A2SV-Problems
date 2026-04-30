class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        c = 0
        pro = 1

        for r in range(len(nums)):
            pro *= nums[r]

            while l <= r and pro >= k:
                pro /= nums[l]
                l += 1
            
            c += r - l + 1
        
        return c
        