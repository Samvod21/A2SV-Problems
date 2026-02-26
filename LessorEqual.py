n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = -1

count = 0

for i in range(1, 10**9):
    for j in a:
        if j < i:
            count += 1

    if count == k:
        ans = i
        break

    count = 0

print(i)
    

    
