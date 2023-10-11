def fibonacci_sequence(n):
    sequence = [1, 2]
    while sequence[-1] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:-1]

def reduce_fibonacci(n):
    sum = 0
    new_list = []
    storage = fibonacci_sequence(n)
    while True:
        if sum == n:
            break
        elif sum + storage[-1] <= n:
            sum += storage[-1]
            new_list.append(storage[-1])
            storage.pop()
        else:
            storage.pop()
    return new_list
    
        

n = int(input())
final = fibonacci_sequence(n)
check = reduce_fibonacci(n)
final_res = []
for i in check:
    count = 1
    for j in final:
        if i == j:
            final_res.append(count)
            break
        count += 1
print(*final_res)
