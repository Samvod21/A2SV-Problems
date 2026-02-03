def isSubset(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
        
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
        i += 1
        
    if j == len(b):
        return True
        
    return False

a = [1,2,3,4,5]
b = [1,1]
print(isSubset(a,b))
#21 3