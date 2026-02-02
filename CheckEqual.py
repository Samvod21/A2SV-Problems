def checkEqual(a, b) -> bool:
    a.sort()
    b.sort()
    size = 0
        
    for i in a:
        size += 1
        
    for i in range(0, size):
        if a[i] != b[i]:
            return False
        
    return True

a = [1,2,4,3,5]
b = [5,4,2,3,1]

print(checkEqual(a,b))