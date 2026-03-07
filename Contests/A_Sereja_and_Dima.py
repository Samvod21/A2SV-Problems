n = int(input())
arr = list(map(int, input().split()))
#arr.sort()
ans = []
s = 0
d = 0
r = 0
l = n - 1

for i in range(n):
    if i % 2 == 0:
        if arr[r] > arr[l]:
            s += arr[r]
            r += 1

        else:
            s += arr[l]
            l -= 1
    
    else:
        if arr[r] > arr[l]:
            d += arr[r]
            r += 1
        
        else:
            d += arr[l]
            l -= 1

ans.append(s)
ans.append(d)

for i in ans:
    print(i, end=' ')
