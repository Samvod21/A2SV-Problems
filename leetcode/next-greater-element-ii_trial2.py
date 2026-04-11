class Solution(object):
    def nextGreaterElements(self, nums):
        ans = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                first = stack.pop()
                ans[first] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                first = stack.pop()
                ans[first] = nums[i]

        return ans
        