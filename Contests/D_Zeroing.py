n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

for i in range(k):
    minimum = min(arr)

    if minimum == 0:
        for i in arr:
            if i > 0:
                ans.append(i)

                for j in range(n):
                    if arr[j] != 0:
                        arr[j] = arr[j] - i
            
    
    else:
        ans.append(minimum)
        for i in range(n):
            arr[i] = arr[i] - minimum

for i in ans:
    print(i)
    
    