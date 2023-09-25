def counter(n):
    k = 0
    while n != 0:
        n = n // 10
        k += 1
    return k

k = int(input())
i = 1
c = 0

while True:
    c += counter(i)
    if c >= k:
        break
    i += 1

if k == c:
    print(i % 10)
else:
    c = c - k
    for j in range(1, c + 1):
        i = i // 10
    print(i % 10)