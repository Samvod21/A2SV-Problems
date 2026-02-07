n = int(input())
s = input()
genome = "ACTG"
count = 0

if n == 4:
    for i in range(0, 4):
        if s[i] != genome[i]:
            count += 1
    
    print(count)
else:
    sub = s[-4::]

    for i in range(0,4):
        if sub[i] != genome[i]:
            count += 1
    
    rest = len(s) - 4
    print(rest * count)




