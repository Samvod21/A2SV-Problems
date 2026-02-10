class Solution(object):
    def buildArray(self, nums):
        ans = []

        for i in range(0, len(nums)):
            ans.insert(i, nums[nums[i]])
        
        return ans
    
test = Solution()
result = test.buildArray([5,0,1,2,3,4])
print(result)
#2 5