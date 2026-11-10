def fibonacci_series(n):
    next_terms = lambda first, second: (second, first + second)
    first, second = 0, 1
    series = []

    for _ in range(n):
        series.append(first)
        first, second = next_terms(first, second)

    return series


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    print(*fibonacci_series(n))