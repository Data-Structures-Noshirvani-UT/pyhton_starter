N = 100 + 10
f_ = [-1] * N
g_ = [-1] * N

def f(n):
    if f_[n] + 1:
        return f_[n]
    f_[n] = f(n - 2) + 2 * g(n - 1)
    return f_[n]

def g(n):
    if g_[n] + 1:
        return g_[n]
    g_[n] = f(n - 1) + g(n - 2)
    return g_[n]

f_[1] = 0
f_[2] = 3
f_[3] = 0

g_[1] = 1
g_[2] = 0

n = int(input())
print(2 * f(n))
