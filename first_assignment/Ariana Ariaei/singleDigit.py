x = int(input())
sum = 0
while x > 0 or sum > 9:
    if x == 0:
        x = sum
        sum = 0
    sum += x % 10
    x //= 10
print(sum)
