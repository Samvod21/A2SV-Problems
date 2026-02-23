from collections import Counter

n = int(input())
pairs = []

for i in range(n):
    num = int(input())

    for j in range(num):
        s = input()
        pairs.append(s)

sizes = Counter(pairs)
max_size = max(sizes.values())

RCR = (max_size / n) * 100

if RCR >= 80:
    print("YES")
else:
    print("NO")