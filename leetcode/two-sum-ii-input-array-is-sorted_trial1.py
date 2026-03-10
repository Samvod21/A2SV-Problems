class Solution(object):
    def twoSum(self, numbers, target):
       l = 0
       r = len(numbers) - 1

       while l < r:
        if numbers[r] + numbers[l] == target:
            return [l + 1, r + 1]
        
        elif target < numbers[r] + numbers[l]:
            r -= 1
        
        else:
            l += 1