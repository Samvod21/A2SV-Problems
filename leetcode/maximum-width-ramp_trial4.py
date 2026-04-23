class Solution(object):
    def maxWidthRamp(self, nums):
        maximum = 0
        stack = []

        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
            
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ind = stack.pop()
                maximum = max(maximum, i - ind)
        
        return maximum

        