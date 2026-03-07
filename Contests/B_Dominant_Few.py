n = int(input())
ans = []

for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    elite = arr[size - 1]
    l = size - 2
    f = size - 3

    while f >= 0:
        if arr[l] + arr[f] < elite:
            ans.append("YES")
            break
        
        f -= 1
        l -= 1
    
    ans.append("NO")


for i in ans:
    print(i)