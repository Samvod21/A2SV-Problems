from collections import Counter

n = int(input())
ans = []
#s = 0
    
for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    minimum = int(10e9)
        
    for i in range(1, size - 1):
        m1 = abs(arr[i] - arr[i - 1]) + abs(arr[i + 1] - arr[i])
        minimum = min(minimum, m1)
        
    print(minimum)


        




