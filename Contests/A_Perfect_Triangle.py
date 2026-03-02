from collections import Counter

def PerfectTriangle(ans):
    n = int(input())
    #ans = []
    s = 0
    
    for i in range(n):
        size = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        arr1 = set(arr)
        arr2 = list(arr1)
        size1 = len(arr1)
        minimum = arr[0]
        maximum = arr[size - 1]
        count = Counter(arr)
        
        for key, val in count.items():
            if val >= 3:
                ans.append(0)
                break
        
            elif val == 2:
                if key == minimum:
                    for i in arr2:
                        if i > key:
                            diff = i - key
                            ans.append(diff)
                            break
            
                elif key == maximum:
                    for i in range(size1 - 1, -1, -1):
                        if arr2[i] < key:
                            diff1 = key - arr2[i]
                            ans.append(diff1)
                            break
                else:
                    for i in range(size1):
                        if key == arr2[i]:
                            diff2 = key - arr2[i - 1]
                            break
                    
                    for j in arr2:
                        if j > key:
                            diff3 = j - key
                
                    mini = min(diff2, diff3)
                    ans.append(mini)
                    break

            else:
                diff4 = arr2[1] - arr2[0]
                diff5 = arr2[2] - arr2[1]
                s = diff4 + diff5
                ans.append(s)
                break


answer = []
PerfectTriangle(answer)

for i in answer:
    print(i)


