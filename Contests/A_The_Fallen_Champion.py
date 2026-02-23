wy, ty = map(int, input().split())
n = int(input())
win = True

for i in range(n):
    x, y = map(int, input().split())

    if wy < x:
        win = False
    
    if wy == x:
        if ty > y:
            win = False

if win:
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")
    
    
        

