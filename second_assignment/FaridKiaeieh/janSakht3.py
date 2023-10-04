def is_prime(n): return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
def generate_hard_passwords(n, password=""): 
    if len(password) == n: print(password); return 
    for digit in range(10): 
        if is_prime(int(password + str(digit))): generate_hard_passwords(n, password + str(digit))
n = int(input()); generate_hard_passwords(n)
