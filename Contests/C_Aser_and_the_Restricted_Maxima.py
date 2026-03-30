t = int(input())
ans = []

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    maxones = 0
    ones = 0

    for i in s:
        if i == 1:
            ones += 1
            
            if ones >= k:
                ans.append("NO")
                break
        else:
            ones = 0
    
    ambitious = [i for i, val in enumerate(s) if val == 1]
    safe = [i for i, val in enumerate(s) if val == 0]
    p = [0] * n

    for i, ind in enumerate(ambitious):
        p[ind] = i + 1
    
    next = len(ambitious) + 1

    for i, ind in enumerate(safe):
        p[ind] = next + i
    
    ans.append("YES")
    ans.append(p)

for i in ans:
    print(i)
        
        