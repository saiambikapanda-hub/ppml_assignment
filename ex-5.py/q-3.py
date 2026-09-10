"""WAP to enter a dictionary and remove the duplicate values inside the dictionary."""

def remove_duplicates(d):
    new_dict = {}

    for key in d:
        if d[key] not in new_dict.values():
            new_dict[key] = d[key]

    return new_dict


d = eval(input("Enter a dictionary: "))

result = remove_duplicates(d)

print("Dictionary after removing duplicate values:", result)
