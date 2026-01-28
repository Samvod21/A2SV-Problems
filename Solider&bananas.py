a, b, c = map(int, input().split())
sum = 0

for i in range(1, c + 1):
    sum += i * a

print(sum - b)