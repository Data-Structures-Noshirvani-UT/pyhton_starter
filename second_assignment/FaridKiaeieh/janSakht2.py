def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_hard_passwords(n):
    start = 10**(n-1)
    end = 10**n
    passwords = []

    for num in range(start, end):
        flag = True
        s_num = str(num)
        n_len = (len(s_num))
        for j in range(n_len, 0, -1):
            if is_prime(int(s_num[0:j])):
                pass
            else :
                flag = False
        if flag:
            passwords.append(num)

    return passwords

n = int(input())

passwords = generate_hard_passwords(n)

for password in passwords:
    print(password)
