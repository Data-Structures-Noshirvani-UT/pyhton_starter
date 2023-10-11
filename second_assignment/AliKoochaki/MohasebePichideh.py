def comp(n, k):
    nSum = 1
    kSum = 1
    for i in range(k):
        nSum *= n
        kSum *= k
        n -= 1
        k -= 1
    return round(nSum / kSum)


numbers = input().split(" ")
a = int(numbers[0])
x = int(numbers[1])
n = int(numbers[2])
sum = 0
for i in range(0, n + 1):
    sum += comp(n, i) * (x ** i) * (a ** (n - i))
print(sum)