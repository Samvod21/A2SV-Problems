def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
        
    if len(s1) != len(s2):
        return False

    ind = []

    for i, j in zip(s1, s2):
        if i != j:
            ind.append((i, j))
        
    if len(ind) == 2 and ind[0] == ind[1][::-1]:
        return True
        
    return False

print(areAlmostEqual("bank", "kanb"))