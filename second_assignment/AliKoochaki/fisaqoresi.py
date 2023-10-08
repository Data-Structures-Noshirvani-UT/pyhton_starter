import math

n = int(input())

mod = 1
if n % 100 == 0 and n > 10000:
    n = n // 100
    mod = 100
m = 0
for i in range(3, n):
    for j in range(i + 1, n):
        m = i + j + math.sqrt(i * i + j * j)
        if m > n:
            break
        if m == n:
            print(i * mod, j * mod, round(math.sqrt(i * i + j * j)) * mod)
            exit()
print("Impossible")