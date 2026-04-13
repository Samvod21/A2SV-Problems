from collections import Counter

n, m = map(int, input().split())
answers = [list(input()) for _ in range(n)]
points = list(map(int, input().split()))
maximum = 0

for i, stuans in enumerate(zip(*answers)):
    counts = Counter(stuans)
    correctstu = max(counts.values())
    maximum += correctstu * points[i]

print(maximum)



