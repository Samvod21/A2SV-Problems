def insertionSort1(n, arr):
    for i in range(n):
        val = arr[i]
        j = i - 1
        
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
            print(*arr)
        
        arr[j + 1] = val
    
    print(*arr)    
        
        
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)