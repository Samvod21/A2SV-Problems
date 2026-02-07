n = int(input())
counts = []

for i in range(0, n):
    bis = int(input())
    count = 0

    for Alice in range(bis - 1, bis // 2, -1):
        for Betty in range(1, (bis // 2) + 1):
            if Alice > Betty and Alice + Betty == bis:
                count += 1
    
    counts.append(count)

for i in counts:
    print(i)