class Solution(object):
    def minOperations(self, nums):
        minimum = len(nums)
        uni = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[uni] = nums[i]
                uni += 1
        
        j = 0

        for i in range(uni):
            while j < uni and nums[j] - nums[i] <= len(nums) - 1:
                j += 1
            
            minimum  = min(minimum, len(nums) - j + i)
        
        return minimum
        