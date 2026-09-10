"""wap to enter two difference sets with string elements combine both the sets remove  any duplicates are present print the new set"""

def combine_sets(s1, s2):
    new_set = set()

    for element in s1:
        new_set.add(element)

    for element in s2:
        new_set.add(element)

    return new_set


s1 = eval(input("Enter first set: "))
s2 = eval(input("Enter second set: "))

result = combine_sets(s1, s2)

print("New set:", result)
