n = int(input())
nums = list(map(int, input().split()))
nums.sort()
res = []
high = 0
low = 0

for i in range(n - 1, -1, -2):
    high += nums[i]

for j in range(n - 2, -1, -2):
    low += nums[j]

print(high)
print(low)


