s = input()
t = input()

if len(s) != len(t):
    print("No")

else:
    vowels = "aeiou"
    is_possible = True

    for i, j in zip(s, t):
        if i in vowels and j not in vowels:
            is_possible = False
            break

        elif i not in vowels and j in vowels:
            is_possible = False
            break

    if is_possible:
        print("Yes")
    
    else:        
        print("No")
