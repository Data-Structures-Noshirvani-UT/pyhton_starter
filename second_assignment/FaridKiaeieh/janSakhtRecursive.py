def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_hard_passwords(n, password=""):
    if len(password) == n:
        print(password)
        return

    for digit in range(10):
        new_password = password + str(digit)
        if is_prime(int(new_password)):
            generate_hard_passwords(n, new_password)

n = int(input())
generate_hard_passwords(n)