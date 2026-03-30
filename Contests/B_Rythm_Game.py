t = int(input())
ans = []

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    if 1 not in s:
        ans.append(0)
    
    else:
        ind = s.index(1)
        c = 1
    
        for i in range(ind + 1, n):
            if s[i] == 1:
                start = max(0, i - (k - 1))
                prev = s[start: i]

                if 1 not in prev:
                    c += 1
    
        ans.append(c)

for i in ans:
    print(i)




    