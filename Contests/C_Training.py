n = int(input())
problems = list(map(int, input().split()))
problems.sort()
days = 1

for q in problems:
    if q >= days:
        days += 1

print(days - 1)
