import math
n, k = map(int, input().split())
# n = p + x (p is how many times smn put a candy, and x is the taken amount)

a = 1
b = 3
c = -2 * n - 2 * k

delta = b * b - 4 * a * c
sqrt_delta = math.isqrt(delta)
# s1 = (-b - sqrt_delta) // (2*a)

s2 = (-b + sqrt_delta) // (2 * a)
# we solved for p, back to x, x = n - p 
x = n - s2


print(x)