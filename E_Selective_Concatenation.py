nt = int(input())
#b = set()
res = []

for i in range(nt):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    m = k // 2

    if 2 * m == n:
        for i in range(1, n, 2):
            if arr[i] != (i + 1) // 2:
                res.append((i + 1) // 2)
                break
        else:
            res.append(m + 1)
    else:
        limit = n - 2 * m + 1
        for i in range(1, limit):
            if arr[i] != 1:
                res.append(1)
                break
        else:
            res.append(2)

for i in res:
    print(i)