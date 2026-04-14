n, m = map(int, input().split())
bus_stops = list(map(int, input().split()))
c = 1
capacity = 0

for i in bus_stops:
    if i + capacity <= m:
        capacity += i
    else:
        c += 1
        capacity = i
print(c)