""" wap  to find the ratio of positive numbers, negative numbers and zeros in an array of integers using 
map()"""

# Program to find the ratio of positive numbers,
# negative numbers and zeros using map()

numbers = [10, -5, 0, 8, -2, 0, 6, -7, 4]

# Find positive, negative and zero using map()
positive = list(map(lambda x: x > 0, numbers))
negative = list(map(lambda x: x < 0, numbers))
zero = list(map(lambda x: x == 0, numbers))

# Count True values
p = sum(positive)
n = sum(negative)
z = sum(zero)

total = len(numbers)

print("Array:", numbers)
print("Positive numbers:", p)
print("Negative numbers:", n)
print("Zeros:", z)

print("Ratio of positive numbers:", p, "/", total)
print("Ratio of negative numbers:", n, "/", total)
print("Ratio of zeros:", z, "/", total)
