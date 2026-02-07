n = int(input())
Colonies = []
A = 0
B = 0
res = []

for i in range(0, n):
    part = int(input())

    if part % 2 == 0:
        gro = part // 2

        for i in range(0, gro):
           Colonies.append(2)
    
    elif part % 3 == 0:
        gro = part // 3
        
        for i in range(0, gro):
            Colonies.add(3)
    
    else:
        gro = part // 3

        for i in range(0, gro):
            Colonies.append(3)
        rest = part % 3

        if rest % 2 == 0:
            gro = rest // 2

            for i in range(0, gro):
                Colonies.append(2)

    for i in range(0, len(Colonies) // 2):
        A += Colonies[i]

    for i in range(len(Colonies) // 2, len(Colonies)):
        B += Colonies[i]
    
    diff = A - B

    if diff < 0:
        diff = -1 * diff
    
    res.append(diff)

for i in res:
    print(i)
    



