class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = float('inf')
        nsum = float('inf')

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                csum = nums[i] + nums[l] + nums[r]
                current = abs(csum - target)
                
                if current < diff:
                    diff = current
                    nsum = csum
                
                if csum < target:
                    l += 1
                
                else:
                    r -= 1
        
        return nsum
        
        