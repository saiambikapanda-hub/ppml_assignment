"""wap to convert a given list of integer and tuple of integer in a list of string using map()"""
# Program to convert a list of integers and a tuple of integers
# into a list of strings using map()

list1 = [10, 20, 30, 40]
tuple1 = (50, 60, 70, 80)

# Convert list of integers into list of strings
result_list = list(map(str, list1))

# Convert tuple of integers into list of strings
result_tuple = list(map(str, tuple1))

print("List of integers:", list1)
print("List of strings:", result_list)

print("Tuple of integers:", tuple1)
print("List of strings:", result_tuple)
