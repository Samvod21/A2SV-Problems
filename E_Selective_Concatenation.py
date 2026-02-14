nt = int(input())
b = set()
res = []

for i in range(nt):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    for j in arr:
        b.add(j)
    
    b.add(0)

    anb = list(b)

    for i in range(0, len(anb)):
        if anb[i] != i + 1:
            res.append(i + 1)

for i in res:
    print(i)