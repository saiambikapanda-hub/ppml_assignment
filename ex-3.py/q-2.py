# Factorial number

n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("Factorial of", n, "is", fact)
else:
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is", fact)
