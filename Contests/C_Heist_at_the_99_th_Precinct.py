from collections import Counter

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    count = Counter(arr)

    for key, value in count.items():
        if value % 2 != 0:
            ans.append("YES")
            break
    
    else:
        ans.append("NO")

for i in ans:
    print(i)
            