n = int(input())
ans = []

for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))

    if size == 1:
        ans.append("YES")
    else:
        arr.sort()

        for i in range(0, size - 1):
            if arr[i + 1] - arr[i] > 1:
                ans.append("NO")
                break
        else:            
            ans.append("YES")
        

                             
                
            

for res in ans:
    print(res)