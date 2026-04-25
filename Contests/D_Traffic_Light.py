t = int(input())
ans = []
maximum = 0

for _ in range(t):
    n, c = input().split()
    s = input()
    n = int(n)

    if n == 1:
        ans.append(0)
        exit()
    
    #c = chr(c)
    con = s + s
    size = n * 2

    for i in range(size - 1, -1, -1):
        if con[i] == c:
            ind = i
            break


    for i in range(ind + 1):
        count = 0

        if con[i] == c:
            while con[i] != 'g':
                count += 1
            
        maximum = max(maximum, count)
    
    ans.append(maximum)

for i in ans:
    print(i)
            




