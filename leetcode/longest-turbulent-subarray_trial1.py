class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) <= 1:
            return len(arr)
        
        l = 0
        r = 0
        maximum = 1
        p = '='

        while(r < len(arr)):
            if arr[r - 1] < arr[r] and p != '<':
                maximum = max(maximum, r - l + 1)
                p = '<'
                r += 1
            
            elif arr[r - 1] > arr[r] and p != '>':
                maximum = max(maximum, r - l + 1)
                p = '>'
                r += 1
            
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r += 1
                
                else:
                    l = r - 1
                p = '='
        
        return maximum
        