def majorityElement(nums):
        nums.sort()
        size = len(nums)
        
        return nums[size // 2]