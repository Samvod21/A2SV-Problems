class Solution(object):
    def removeElement(self, nums, val):
        c = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        
        return c
        