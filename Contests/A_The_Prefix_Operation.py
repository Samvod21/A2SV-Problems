t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    s = list(input())
    c = s.count('B')

    if c == k:
        print(0)
        continue
    
    for i in range(1, n + 1):
        temp = s[:]
        temp[:i] = ['A'] * i

        if temp.count('B') == k:
            print(1)
            print(i, 'A')
            break   

        temp = s[:]
        temp[:i] = ['B'] * i

        if temp.count('B') == k:
            print(1)
            print(i, 'B')
            break

        