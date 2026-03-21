def cheakPalindrome(s):
    s1 = s
    s.reverse()
    c = 0
    
    for i, j in zip(s, s1):
        if i != j:
            c += 1
            
    if c != 0:
        return False
    else:
        return True
    

t = int(input())
ans = []

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    c = 0

    while c == 0:
        for i in range(0, n):
            for j in range(i + 1, n):
                s1 = s[i:j + 1]
                
                for k in range(0, len(s1)):
                    if s1[k] == 0:
                        s1[k] = 1
                    else:
                        s1[k] = 0

            res = cheakPalindrome(s1)

            if res == True:
                c += 1
    
    if c != 0:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)