class NumArray(object):

    def __init__(self, nums):
        self.total = [0] * len(nums)
        self.total[0] = nums[0]

        for i in range(1, len(nums)):
            self.total[i] = self.total[i - 1] + nums[i]
        

    def sumRange(self, left, right):
        if left == 0:
            return self.total[right]

        return self.total[right] - self.total[left - 1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)