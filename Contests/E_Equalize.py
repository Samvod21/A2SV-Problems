from collections import Counter

t = int(input())
maxs = []
ans = []

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    for i in range(n):
        arr[i] += i + 1
    
    c = Counter(arr)

    for k, v in c.items():
        maxs.append(v)
    
    ans.append(max(maxs))

for i in ans:
    print(i)

    
