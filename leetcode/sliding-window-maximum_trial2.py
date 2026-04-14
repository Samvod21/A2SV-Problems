class Solution(object):
    def maxSlidingWindow(self, nums, k):
        maxes = []
        queue = deque()

        for i, val in enumerate(nums):
            while queue and queue[-1] < val:
                queue.pop()
            queue.append(val)

            if i >= k and nums[i - k] == queue[0]:
                queue.popleft()
            
            if i >= k - 1:
                maxes.append(queue[0])
        
        return maxes
             