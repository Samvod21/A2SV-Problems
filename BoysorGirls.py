user_name = input()
letters = set()
count = 0

for i in user_name:
    letters.add(i)
    
for j in letters:
    count += 1
    
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")


