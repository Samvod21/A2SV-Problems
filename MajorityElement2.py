from collections import Counter

class Solution(object):
   def majorityElement(self, nums):
        count = Counter(nums)
        freq = []
        
        for i, fre in count.items():
            if fre > len(nums) / 3:
                freq.append(i) 


        return freq

s = Solution()
a = [3,2,3,4,4]

print(s.majorityElement(a))
# 5 30