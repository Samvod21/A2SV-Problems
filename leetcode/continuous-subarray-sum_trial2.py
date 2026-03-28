class Solution(object):
    def checkSubarraySum(self, nums, k):
        c = 0
        f = {0: -1}

        for i, j in enumerate(nums):
            c += j
            rem = c % k

            if rem in f:
                if i - f[rem] >= 2:
                    return True
            
            else:
                f[rem] = i
        
        return False

        