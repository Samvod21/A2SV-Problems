class Solution(object):
    def findRightInterval(self, intervals):
        starts = []

        for i in range(len(intervals)):
            starts.append((intervals[i][0], i))
        
        starts.sort()
        ans = []

        for start, end in intervals:
            l, r = 0, len(intervals) - 1
            ind = -1

            while l <= r:
                mid = l + (r - l) // 2

                if starts[mid][0] >= end:
                    ind = starts[mid][1]
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            ans.append(ind)
        
        return ans


        