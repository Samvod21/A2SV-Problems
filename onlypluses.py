n = int(input())
arr = []
res = []

for i in range(0, n):
    a, b, c = map(int, input().split())
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.sort()
    
    for i in range(0, 5):
        arr[0] = arr[0] + 1
        arr.sort()
    
    res.append(arr[0] * arr[1] * arr[2])

for j in res:
    print(j)
