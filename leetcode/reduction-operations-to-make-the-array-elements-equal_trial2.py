class Solution(object):
    def reductionOperations(self, nums):
        minimum = min(nums)
        size = len(nums)
        count = 0
        res = 0
        nums.sort()
        #dist = set(nums)
        
        for i in range(1, size):
                if nums[i] != nums[i - 1]:
                    count += 1
                
                res += count
        
        return res
        


        