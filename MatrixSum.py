class Solution(object):
    def matrixSum(self, nums):
        sum = 0
        cols = []

        for i in nums:
            i.sort()
        
        for i in range(len(nums[0])):
            for j in range(len(nums)):
                cols.append(nums[j][i])
        
            maximum = max(cols)
            sum += maximum
            cols = []
    
        return sum
# 2 39