h = int(input())
arr = list(map(int, input().split()))
max_len = 0
current_len = 0
arrnext = arr + arr

for i in arrnext:
    if i == 1:
        current_len += 1
        max_len = max(max_len, current_len)
    
    else:
        current_len = 0


print(min(max_len, h))