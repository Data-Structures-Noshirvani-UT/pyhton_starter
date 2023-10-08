def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input())

fiboElements = []
for i in range(1, n + 1):
    if fibo(i) <= n:
        fiboElements.append(fibo(i))
    else:
        break

for i in range(len(fiboElements) - 1, -1, -1):
    if fiboElements[i] <= n:
        n -= fiboElements[i]
        print(i, end=" ")