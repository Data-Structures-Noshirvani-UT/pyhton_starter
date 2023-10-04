from math import factorial

a, x, n = input().split(" ")
n = int(n)
a = int(a)
x = int(x)
sum = 0
for k in range(n + 1):
    formula = int((factorial(n) / (factorial(n - k) * factorial(k))) * (x**k) * (a**(n - k))) 
    sum += formula
print(sum)