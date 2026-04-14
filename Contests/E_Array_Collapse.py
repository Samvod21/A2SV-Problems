t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    s = input().strip()
    l = 0
    r = n - 1
    order=[]

    for i in s:
        if i=="L":
            order.append(a[l])
            l += 1

        else:
            order.append(a[r])
            r -= 1
            1
    res = [0] * n
    pre = 1

    for i in range(n - 1, -1, -1):
        pre = (pre * order[i]) % k
        res[i] = pre

    print(*res)