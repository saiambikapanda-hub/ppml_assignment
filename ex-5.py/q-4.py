"""wap to enter a set and copy the content of the set into a new set one element at a time."""

def copy_set(s):
    new_set = set()

    for element in s:
        new_set.add(element)

    return new_set


s = eval(input("Enter a set: "))

result = copy_set(s)

print("Original set:", s)
print("New set:", result)
