n = int(input())
m = int(input())
change = 0
k = m
for i in range(2, n + 1):
    m = int(input())
    if k != m:
        k = m
        change += 1
print(change)