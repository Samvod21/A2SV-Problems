class Solution(object):
    def smallestDivisor(self, nums, threshold):
        l = 1
        maximum = max(nums)

        while l < maximum:
            mid = l + (maximum - l) // 2
            total = 0

            for i in nums:
                total += (i + mid - 1) // mid
            
            if total > threshold:
                l = mid + 1
            
            else:
                maximum = mid
        
        return l


        