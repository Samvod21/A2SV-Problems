n, mission = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
 
left = 0
right = len(arr) - 1
total = 0 
while left <= right:
    current = mission // arr[right] + 1
    if right - left + 1< current:
        break
    total += 1
    left += current - 1 
    right -= 1
 
print(total)