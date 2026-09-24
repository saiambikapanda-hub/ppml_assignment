# Twin prime numbers between 1 to N

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input("Enter the value of N: "))

print("Twin prime numbers between 1 and", N, "are:")

for i in range(2, N - 1):
    if is_prime(i) and is_prime(i + 2) and (i + 2) <= N:
        print(f"({i}, {i + 2})")
