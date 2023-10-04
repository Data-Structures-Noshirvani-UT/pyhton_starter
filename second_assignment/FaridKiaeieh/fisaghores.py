def check(n):
    epsilon = 1e-9
    for a in range(1, n//2 + 1):
        b = (n**2 - 2*n*a) / (2*(n - a))
        if b - int(b) < epsilon and b > 0:
            b = int(b)
            c = n - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)
    return None

n = int(input())
result = check(n)

if result:
    print(" ".join(map(str, result)))
else:
    print("Impossible")
