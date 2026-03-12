class Solution(object):
    def removeDuplicates(self, nums):
        c = 0
        size = len(nums)

        for i in range(1, size):
            if nums[i] != nums[c]:
                c += 1
                nums[c] = nums[i]
        
        return c + 1