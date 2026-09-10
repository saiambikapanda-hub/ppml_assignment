""" WAP to create a dictionary and print the key which has the maximum unique values."""

def max_unique_value(d):
    max_key = None
    max_count = 0

    for key in d:
        unique_values = set(d[key])
        count = len(unique_values)

        if count > max_count:
            max_count = count
            max_key = key

    return max_key


d = {
    'A': [10, 20, 10, 30],
    'B': [40, 50, 60, 40],
    'C': [70, 70, 80]
}

result = max_unique_value(d)

print("Key having maximum unique values:", result)
