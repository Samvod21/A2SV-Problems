n = int(input())
s = input()
count = 0

if n < 26:
    print("No")
else:
    lowstr = s.lower()
    lett = set()

    for i in lowstr:
        lett.add(i)
    
    for j in lett:
        count += 1
    
    if count >= 26:
        print("YES")
    else:
        print("NO")
    
