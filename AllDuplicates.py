from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):
        num = Counter(nums)
        dup = []

        for key, val in num.items():
            if val > 1:
                dup.append(key)
        
        return dup
#1 1