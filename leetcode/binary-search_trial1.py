class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            half = (l + r) // 2

            if nums[half] == target:
                return half
            
            elif nums[half] < target:
                l = half + 1
            
            else:
                r = half - 1
        
        return -1
            
        