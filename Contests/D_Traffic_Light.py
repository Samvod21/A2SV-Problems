t = int(input())
ans = []

for _ in range(t):
    n, c = input().split()
    s = input()
    n = int(n)

    if n == 1:
        ans.append(0)
        continue
    # Find the first 'g'
    first_g = -1

    for i in range(n):
        if s[i] == 'g':
            first_g = i
            break
    
    if first_g == -1:
        # No 'g', but assume there is
        ans.append(0)
        continue
    
    # Precompute next_g
    next_g = [0] * n
    last_g = first_g + n  # for circular

    for i in range(n-1, -1, -1):
        if s[i] == 'g':
            next_g[i] = i
            last_g = i

        else:
            next_g[i] = last_g
    
    # Now find max wait for 'c'
    maximum = 0
    
    for i in range(n):
        if s[i] == c:
            wait = next_g[i] - i
            maximum = max(maximum, wait)
    
    ans.append(maximum)

for i in ans:
    print(i)
            




