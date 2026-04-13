t = int(input())
n, k = map(int, input().split())
s = input()
ans = []

for _ in range(t):
    if s.count('B') == k:
        ans.append(0)
    
    else:
        if s.count('B') < k:
            if k == n:
                ans.append(1)
                ans.append([n, 'A'])
            else:
                ans.append(2)
                ans.append([n, 'A'], [k, 'B'])
        else:
            if k == 0:
                ans.append(1)
                ans.append([n, 'A'])
            else:
                ans.append(2)
                ans.append([n, 'B'], [n - k, 'A'])

for a in ans:
    print(a)
            
    
        