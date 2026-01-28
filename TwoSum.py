def twoSum(nums, target):
    ans = []
    size = len(nums)

    for i in range(0, size):
        for j in range(i + 1, size):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
        
    return ans
numbers = [1, 2, 5, 6, 8]
res = twoSum(numbers, 14)

for i in res:
    print(i)