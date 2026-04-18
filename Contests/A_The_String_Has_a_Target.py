t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    s = input()
    minimum = min(s)

    for i in range(n - 1, -1, -1):
        if s[i] == minimum:
            ind = i
            break
    
    l = s[:ind]
    r = s[ind + 1:]
    ans.append(minimum + l + r)

for i in ans:
    print(''.join(i))