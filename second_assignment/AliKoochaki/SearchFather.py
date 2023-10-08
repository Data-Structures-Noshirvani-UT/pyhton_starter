def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sumOfPrimeFactors(num):
    sumOfFactors = 0
    for i in range(2, num + 1):
        if num % i == 0 and isPrime(i):
            sumOfFactors += i
    return sumOfFactors


def sumOfDigitOfNumber(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def haveFather(n):
    for i in range(num):
        d = i + sumOfDigitOfNumber(i) + sumOfPrimeFactors(i)
        if d == n:
            return True
    return False


t = int(input())

for i in range(t):
    num = int(input())
    if haveFather(num):
        print("Yes")
    else:
        print("No")