class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []

        if len(nums) < 3:
            return []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                res = nums[l] + nums[r] + nums[i]

                if res == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                
                    l += 1
                    r -= 1
                
                elif res < 0:
                    l += 1
                
                else:
                    r -= 1
        
        return ans