n = int(input())


def nextPowerOf2(n):
    k = 1
    while k <= n:
        k = k << 1

    return k


print(nextPowerOf2(n))
