t = int(input())
ans = []

for i in range(t):
    n, k = map(int, input().split())
    bracos = [0] * (k + 1)

    for j in range(k):
        b, c = map(int, input().split())
        bracos[b] += c
    
    #bracos.sort(reverse=True)

    if n >= k:
        s = 0

        for y in bracos:
            s += y
        
        ans.append(s)
    
    else:
        s1 = 0
        bracos.sort(reverse=True)

        for i in range(n):
            s1 += bracos[i]
        
        ans.append(s1)

for i in ans:
    print(i)

