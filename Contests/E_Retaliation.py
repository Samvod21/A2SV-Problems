t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    consistency = a[1] - a[0]
    broken = False

    for i in range(1, n):
        if a[i] - a[i - 1] != consistency:
            broken = True
            break
    
    if broken:
        ans.append("NO")
    
    else:
        if (a[0] - consistency) % (n + 1) != 0:
            ans.append("NO")
            continue
        
        k = (a[0] - consistency) // (n + 1)
        p = consistency + k

        if p >= 0 and k >= 0:
            ans.append("YES")
        else:
            ans.append("NO")

print(*ans, sep="\n")