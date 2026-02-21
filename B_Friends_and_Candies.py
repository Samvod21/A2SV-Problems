n = int(input())
res = []

for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res.append(str(sum(arr[:m])))
print("\n".join(res))
