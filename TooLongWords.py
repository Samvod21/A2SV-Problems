n = input()
words = [str(input()) for _ in range(n)]

for i in words:
    chars = list(i)
    size = 0;
    
    for j in chars:
        size = size + 1
        
    if size >= 10:
        size = size - 2
        st = str(i[0]) + str(size) + str(i[-1])
        print(st)
    else:
        print(i)

