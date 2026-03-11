class Solution(object):
    def maxArea(self, height):
        size = len(height)
        l = 0
        r = size - 1
        results = []

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            results.append(area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return max(results)

        
        



        