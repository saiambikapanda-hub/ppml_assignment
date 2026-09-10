"""WAP to input two dictionaries and print the values by merging the two dictionaries."""

def merge_dict(d1, d2):
    d1.update(d2)
    return d1

# Input first dictionary
d1 = eval(input("Enter first dictionary: "))

# Input second dictionary
d2 = eval(input("Enter second dictionary: "))

# Merge dictionaries
result = merge_dict(d1, d2)

print("Merged dictionary:", result)
print("Values:", list(result.values()))
