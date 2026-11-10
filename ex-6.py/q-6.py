array1 = list(map(int, input("Enter the elements of the first array: ").split()))
array2 = list(map(int, input("Enter the elements of the second array: ").split()))

intersection = lambda first, second: sorted(set(first) & set(second))
common_elements = intersection(array1, array2)

print("Intersection of the two arrays:")
if common_elements:
    print(*common_elements)
else:
    print("No common elements.")