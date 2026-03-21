t = int(input())
ans = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = False
    c = 0
    
    while f != True:
        br = False

        for i, j in zip(a, b):
            if i > j:
                br = True
                break
        
        if br == True:
            c += 1
            a.insert(0, 0)
            a.pop()

        else:
            f = True
    
    ans.append(c)
    




    

for i in ans:
    print(i)
    

