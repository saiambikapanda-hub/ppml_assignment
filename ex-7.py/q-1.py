"""Wap to triple all numbers in na given list of integers. Use map()"""

# Program to triple all numbers in a list using map()

numbers = [1, 2, 3, 4, 5]

# Logic: multiply each number by 3
def triple(x):
    return x * 3

result = list(map(triple, numbers))

print("Original list:", numbers)
print("Tripled list:", result)
