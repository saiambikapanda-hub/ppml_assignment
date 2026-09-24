#1st 15 terms of fibonacci series without using recursion


def fibonacci():
    a = 0
    b = 1

    print("First 15 terms of Fibonacci series:")

    for i in range(15):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci()
