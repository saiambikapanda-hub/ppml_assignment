"""wap to create a list containing the power of said number in bases raised to the corresponding
number in the index using python map"""

# Program to create a list containing the power of each number
# raised to its corresponding index

numbers = [2, 3, 4, 5, 6]

result = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))

print("Given list:", numbers)
print("Result:", result)
