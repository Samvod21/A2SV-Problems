n, s = map(int, input().split())
a = list(map(int, input().split()))
c = 0
s1 = 0 
l = 0

for r in range(n):
    s1 += a[r]

    while s1 > s and l <= r:
        s1 -= a[l]
        l += 1
    
    c = max(c, r - l + 1)

print(c)
#15

    
    