class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        fres = []
        count = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            
            fres.append(count)
            count = 0 

        return fres              