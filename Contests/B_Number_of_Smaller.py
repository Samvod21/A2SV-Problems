n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
j = 0

for i in arr2:
    while j < n and arr1[j] < i:
        j += 1
    
    result.append(j)


for i in result:
    print(i, end=' ')
    