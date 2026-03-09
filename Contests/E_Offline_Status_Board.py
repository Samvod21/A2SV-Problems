for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))
    dict1 = {v:i for i,v in enumerate(lst)}

    ptr = n-1
    ans = n-1

    while ans>=0:
        if dict1[lst2[ans]]>ptr:
            break

        ptr = dict1[lst2[ans]]
        ans -= 1
    
    print(ans+1)


