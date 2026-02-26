class Solution(object):
    def targetIndices(self, nums, target):
        ind = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                ind.append(i)
        
        return ind
        