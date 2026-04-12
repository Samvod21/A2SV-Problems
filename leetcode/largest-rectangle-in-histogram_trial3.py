class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [-1] * 1
        maximum = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                top = stack.pop()
                length = heights[top]
                width = i - stack[-1] - 1
                maximum = max(maximum, length * width)
            stack.append(i)
        
        while stack[-1] != -1:
            top = stack.pop()
            length = heights[top]
            width = len(heights) - stack[-1] - 1
            maximum = max(maximum, length * width)
        
        return maximum

        