class Solution(object):
    def findMaxAverage(self, nums, k):
        size = len(nums)
        s = 0
        maxavg = float('-inf')

        for i in range(k):
            s += nums[i]
        
        maxavg = float(s) / k
        l = 0

        for r in range(k, size):
            s += nums[r]
            s -= nums[l]

            maxavg = max(maxavg, float(s) / k)
            l += 1
        
        return maxavg
        