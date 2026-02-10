def rotateLeft(d, arr):
    for i in range(0, d):
        front = arr[0]
        arr.pop(0)
        arr.append(front)
    
    return arr

res = rotateLeft(3, [1,2,3,4,5])
print(res)
#1 3