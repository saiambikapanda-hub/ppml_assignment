numbers = list(map(int, input("Enter the list elements: ").split()))
value = int(input("Enter the value to search: "))

is_present = lambda item, values: item in values

if is_present(value, numbers):
    print("{} is present in the list.".format(value))
else:
    print("{} is not present in the list.".format(value))