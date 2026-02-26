n = int(input())
ans = []

for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))

    if size == 1:
        ans.append("YES")
    else:
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            ans.append("YES")
        else:
            ans.append("NO")

for res in ans:
    print(res)