def mutate_string(string, position, character):
    mutated = list(string)
    mutated[position] = character
    
    string = ''.join(mutated)
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

# 6 2