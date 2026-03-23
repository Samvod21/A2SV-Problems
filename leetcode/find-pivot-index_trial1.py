class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        lt = 0
        found = False

        for i in range(len(nums)):
            rt = total - lt - nums[i]
            
            if lt == rt:
                return i
                found = True
                break
            
            lt += nums[i]
        
        if found == False:
            return -1
        
        