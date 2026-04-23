for _ in range(int(input())):
  n, q = map(int,input().split())
  snacks = list(map(int,input().split()))
  snacks.sort(reverse=True)
  tasks = []

  for _ in range(q):
    tasks.append(int(input()))
  prefix = [0] * n
  prefix[0] = snacks[0]

  for i in range(1,n):
    prefix[i] = prefix[i - 1] + snacks[i]

  for t in tasks:

    if t > prefix[n - 1]:
       print(-1)
       continue
    
    l = 0
    r = n-1

    while l < r:
      m = l + (r - l) // 2

      if prefix[m] >= t:
        r = m
      else:
        l = m + 1
    
    print(r + 1)