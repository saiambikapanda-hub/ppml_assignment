# Program to check whether a number is Armstrong or not

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
