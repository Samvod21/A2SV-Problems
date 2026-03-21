k = int(input())
num = list(map(int, input().split()))
#temp = []
sub = []

for i in range(0, len(num)):
    for j in range(i + 1, len(num) + 1):
        val = list(num[i:j])
        sub.append(val)

c = 0

for i in sub:
    if i.count(1) == k:
        c += 1

print(c)


