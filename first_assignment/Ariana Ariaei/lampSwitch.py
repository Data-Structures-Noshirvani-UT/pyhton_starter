n = int(input())
count = 0
list = []
for i in range(0, n):
    x = int(input())
    list.append(x)
for i in range(1, n):
    if list[i] != list[i - 1]:
        count += 1
print(count)
