n, t = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

c = 0
s = 0
l = 0
r = n - 1

while l <= r:
    s += arr[l]

    if s < t:
        c += 1
        l += 1
    
    s += arr[r]

    if s < t:
        c += 1
        r -= 1

print(c)