n = int(input())
s = input()
    
if len(set(s)) < len(s) or n == 1:
    print("Yes")
else:        
    print("No")