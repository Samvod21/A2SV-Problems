def containsDuplicate(nums):
    nums.sort() 
    size = len(nums)
    for i in range(1, size): 
        if nums[i] == nums[i-1]: 
            return True 
    
    return False

nums = [1, 2, 3, 4]
res = containsDuplicate(nums)
print(res)