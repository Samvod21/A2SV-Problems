class Solution(object):
    def searchRange(self, nums, target):
    
        def binarySearch(nums, target, pos):
            l = 0
            r = len(nums) - 1
            ind = -1
        
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
            
                elif nums[mid] < target:
                    l = mid + 1
            
                else:
                    ind = mid

                    if pos == "left":
                        r = mid - 1
                
                    else:
                        l = mid + 1
            
            return ind
        
        l = binarySearch(nums, target, "left")
        r = binarySearch(nums, target, "right")

        return [l, r]
        