def convert_to_base_b(a, b):
    result = ""
    while a > 0:
        digit = a % b
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord('A') + digit - 10) + result
        a //= b
    return result

a ,b = input().split(" ")
a = int(a)
b = int(b)


result = convert_to_base_b(a, b)
iter = len(result)
sum1, sum2 = 0 , 0
for i in range(0, iter, 2):
    sum1 += int(result[i])
for i in range(1, iter, 2):
    sum2 += int(result[i])
if sum1 == sum2:
    print('Yes')
else:
    print('No')