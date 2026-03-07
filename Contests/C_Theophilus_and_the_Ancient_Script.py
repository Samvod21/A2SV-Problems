n = int(input())
ans = []

for i in range(n):
    size = int(input())
    arr = input()
    string = list(arr)
    c = 0
    
    for i in range(size - 1):
        if string[i] == 'A' and string[i + 1] == 'B':
            string[i], string[i + 1] = string[i + 1], string[i]
            c += 1
            i = 0

    ans.append(c)

for i in ans:
    print(i)