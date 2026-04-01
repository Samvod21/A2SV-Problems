class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        c = 1
        arr.sort()

        for i in range(1, len(arr)):
            if arr[i] >= c + 1:
                c += 1
        
        return c
        