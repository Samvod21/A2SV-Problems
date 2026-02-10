N = int(input())

for _ in range(N):
    num = int(input())

    if num <= 3:
        print(num)
    else:
        print(num%2)