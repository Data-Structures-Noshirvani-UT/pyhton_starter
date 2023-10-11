import math


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isHardPass(n):
    while n > 0:
        if not isPrime(n):
            return False
        n //= 10
    return True


n = int(input())
minNumber = 10 ** (n - 1)
maxNumber = 10 ** n
for i in range(minNumber, maxNumber):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        continue
    if isHardPass(i):
        print(i)