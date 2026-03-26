class Solution(object):
    def getAverages(self, nums, k):
        winsize = 2 * k + 1
        ans = [-1] * len(nums)
        s = 0

        if len(nums) < winsize:
            return ans

        for i in range(len(nums)):
            s += nums[i]
        
            if i - winsize >= 0:
                s -= nums[i - winsize]
            
            if i + 1 >= winsize:
                ans[i - k] = s // winsize
        
        return ans
        