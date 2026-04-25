t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)

    ans.append(n * maximum)

for i in ans:
    print(i)