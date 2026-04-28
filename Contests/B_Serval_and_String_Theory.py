t = int(input())
ans = []

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    if s < s[::-1]:
        ans.append("YES")
    
    elif k > 0 and len(set(s)) > 1:
        ans.append("YES")
    
    else:
        ans.append("NO")

print(*ans, sep="\n")