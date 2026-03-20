class Solution(object):
    def runningSum(self, nums):
        runningSum = [0] * (len(nums))

        for i in range(len(nums)):
            runningSum[i] = sum(nums[:i + 1])
        
        return runningSum