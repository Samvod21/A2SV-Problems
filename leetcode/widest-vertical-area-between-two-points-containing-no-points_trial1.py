class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        size = len(points)
        ans = []
        points.sort()

        for i in range(size - 1):
            diff = abs(points[i][0] - points[i + 1][0])
            ans.append(diff)
        
        return max(ans)

        