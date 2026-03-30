t = int(input())
ans = []

for _ in range(t):
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    if s1[0] > s1[1]:
        if s2[0] < s2[1]:
            ans.append("NO")
        else:
            ans.append("YES")
    
    else:
        if s2[0] > s2[1]:
            ans.append("NO")
        else:
            ans.append("YES")

for i in ans:
    print(i)