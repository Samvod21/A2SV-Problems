n = int(input())
result = []

for _ in range(n):
    s = input()
    res = ""

    if len(s) < 10:
        result.append(s)
    
    else:
        middle = str(len(s) - 2)
        res = s[0] + middle + s[-1]
        result.append(res)

for i in result:
    print(i)

