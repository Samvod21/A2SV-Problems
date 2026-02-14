from collections import Counter

nt = int(input())
res = []

for i in range(nt):
    n = int(input())
    arr = list(map(int, input().split()))
    num = set(arr)
    maximum = max(arr)
    countother = 0
    nums = Counter(arr)

    for key, val in nums.items():
        if key != maximum and val >= 2:
            countother += 1
        
        elif key == maximum:
            countmax = val
    
    if countmax >= 2:
        plays = len(num) + countother - (countmax - 1)
        res.append(plays)
    
    else:
        plays = len(num) + countother
        res.append(plays)

for i in res:
    print(i)
    
