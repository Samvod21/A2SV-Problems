t = int(input())
ind = set()
ans = []

for _ in range(t):
    n = int(input())
    stri = list(input().strip())

    for i in range(n - 1):
        if stri[i] == 'A' and stri[i + 1] == 'B':
            ind.add(i)
            stri[i], stri[i + 1] = stri[i + 1], stri[i]
            i = 0
    
    ans.append(len(ind))

for i in ans:
    print(i)
        
    
   
    