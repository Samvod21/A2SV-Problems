def findUnion(a, b):
    set1 = set()
    set2 = set()
        
    for i in a:
        set1.add(i)
        
    for j in b:
        set2.add(j)
        
    return set1 | set2