num, pos = map(int, input().split())
s = ""
nums = []
for i in range(1, num + 1):
    if i % 2 != 0:
        nums.append(i)

for j in range(1, num + 1):
    if j % 2 == 0:
        nums.append(j)
print(nums[pos - 1])
    