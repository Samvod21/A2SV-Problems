class Solution(object):
    def longestSubarray(self, nums, limit):
        l = 0
        maximum = 0
        maxdq = deque()
        mindq = deque()

        for r in range(len(nums)):
            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()
            
            maxdq.append(r)

            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()
            
            mindq.append(r)

            while nums[maxdq[0]] - nums[mindq[0]] > limit:
                l += 1

                if maxdq[0] < l:
                    maxdq.popleft()

                if mindq[0] < l:
                    mindq.popleft()
            
            maximum = max(maximum, r - l + 1)
        
        return maximum

        