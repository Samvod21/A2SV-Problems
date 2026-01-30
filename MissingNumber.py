def missingNumber(nums):
        size = len(nums)
        exp_sum = size * (size + 1) // 2
        real_sum = 0

        for i in nums:
            real_sum += i
        

        return exp_sum - real_sum