class Solution(object):
    def productExceptSelf(self, nums):
        pro = 1
        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] = pro
            pro *= nums[i]
        
        l = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= l
            l *= nums[i]
        
        return ans

        return ans
        

        