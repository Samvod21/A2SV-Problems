n = int(input())
ans = []

for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    for j in range(size - 1):
        f = arr.pop()
        s = arr.pop()

        trans = (f + s) // 2

        arr.insert(0, trans)
    
    if arr[0] == x:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)