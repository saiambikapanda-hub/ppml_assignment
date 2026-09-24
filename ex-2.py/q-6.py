# Program to find all prime factors of a 3-digit number

num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    n = num
    factor = 2

    print("Prime factors are:")

    while n > 1:
        if n % factor == 0:
            print(factor, end=" ")
            n = n // factor
        else:
            factor += 1
else:
    print("Please enter a valid 3-digit number.")
