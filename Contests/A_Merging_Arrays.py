n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

smaller = min(n, m)
bigger = max(n, m)

i = 0
j = 0
ans = []

while i < n and j < m:
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
        #print(i)
    else:
        ans.append(arr2[j])
        j += 1
        #print(j)

for i in range(i, n):
    ans.append(arr1[i])
for j in range(j, m):
    ans.append(arr2[j])





for i in ans:
    print(i, end=' ')