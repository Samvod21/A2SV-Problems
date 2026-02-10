n = int(input())
result = []

for i in range(0, n):
    nums = list(map(int, input().split()))
    nums.sort()

    if nums[0] + nums[1] == nums[2]:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)

#1 5