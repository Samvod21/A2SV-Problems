t = int(input())
ans = []

for _ in range(t):
    s = input()
    
    for i in range(len(s)):
        rest = s[i + 1:]

        if s[i] not in rest:
            res = s[i:]
            break
    
    ans.append(res)

for i in ans:
    print(''.join(i))
    

            




    
    

