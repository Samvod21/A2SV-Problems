class Solution(object):
    def maximumSubarraySum(self, nums, k):
        maxsum = 0
        s = 0
        l = 0
        found = set()
        
        for r in range(len(nums)):
            while nums[r] in found:
                found.remove(nums[l])
                s -= nums[l]
                l += 1

            found.add(nums[r])
            s += nums[r]

            if r - l + 1 >k:
                found.remove(nums[l])
                s -= nums[l]
                l += 1

            if r - l + 1 == k:
                maxsum = max(maxsum, s)
        
        return maxsum

        