class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        l = 0
        r = len(nums) - 1
        c = 0

        while l < r:
            if nums[l] + nums[r] < target:
                c += r - l
                l += 1
                
            else:
                r -= 1
        
        
        return c


        