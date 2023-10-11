def aDarMabnaB(a, b):
    c = 0
    while a > 0:
        c *= 10
        c += a - b * (a // b)
        a //= b
    return int(c)


a, b = input().split(" ")
a = int(a)
b = int(b)
c = aDarMabnaB(a, b)
fard = 0
zoj = 0

i = 1
while c != 0:
    if i % 2 == 1:
        fard += c % 10
    else:
        zoj += c % 10
    c //= 10
    i += 1

if zoj == fard:
    print("Yes")
else:
    print("No")