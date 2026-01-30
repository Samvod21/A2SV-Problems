def containsDuplicate(nums):
    uni = set()

    for i in nums:
        uni.add(i)
        
    if len(nums) == len(uni):
        return False
    else:
        return True

nums = [1, 2, 3, 4]
res = containsDuplicate(nums)
print(res)