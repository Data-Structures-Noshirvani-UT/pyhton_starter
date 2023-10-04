n = int(input())
list = list(range(1, 5000))
str_list = [str(x) for x in list]
str = ''.join(str_list)
print(str[n-1])
