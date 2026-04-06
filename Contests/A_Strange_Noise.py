t = int(input())
ans = []
cat  = "meow"

for _ in range(t):
    n = int(input())
    s = input().lower()
    compressed = s[0]

    for i in range(1, n):
        if s[i] != s[i - 1]:
            compressed += s[i]
    
    if compressed == cat:
        ans.append("YES")
    else:
        ans.append("NO")
    
    
    

for i in ans:    
    print(i)
    