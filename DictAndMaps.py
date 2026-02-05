import sys

n = int(input())
phoneBook = {}

for _ in range(n):
    name, phonenumber = input().split()
    phoneBook[name] = phonenumber

for names in sys.stdin:
    names = names.strip()
    
    if names in phoneBook:
        print(f"{names}={phoneBook[names]}")
    else:
        print("Not found")
# 3 15