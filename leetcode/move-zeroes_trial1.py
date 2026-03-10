class Solution(object):
    def moveZeroes(self, nums):
        size = len(nums)

        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
        