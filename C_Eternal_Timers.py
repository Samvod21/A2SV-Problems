nt = int(input())
res = []

for i in range(nt):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = arr
    minimum = int(min(arr))
    count = 0

    while count != minimum:
        for i in range(n):
            arr2[i] = arr2[i] - 1

            if arr2[i] == 0:
                res.append("NO")
                break
        
        arr2[count // 2] = arr[count // 2]
        count += 1
    
    res.append("YES")

for i in res:
    print(i)
            
