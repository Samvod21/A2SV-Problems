n, t = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
c = 0
l = 0

for r in range(n):
    s += arr[r]

    while s > t:
        s -= arr[l]
        l += 1
    
    c = max(c, r - l + 1)

print(c)