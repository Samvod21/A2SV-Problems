class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        size = len(nums)

        if size < 3:
            if size == 2:
                return nums[1]
            else:
                return nums[0]
        
        
        num = set(nums)
        nums = list(num)
        nums.sort(reverse=True)
        size = len(nums)

        if size < 3:
            if size == 2:
                return nums[0]
            else:
                return nums[0]
        else:
            return nums[2]
        