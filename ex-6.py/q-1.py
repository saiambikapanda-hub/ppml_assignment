import random

def group_similar(matrix):
    elements = []

    # Store all elements in a single list
    for row in matrix:
        for element in row:
            elements.append(element)

    # Sort the elements so similar elements come together
    elements.sort()

    # Convert the list back into a matrix
    rows = len(matrix)
    cols = len(matrix[0])

    grouped_matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[index])
            index += 1
        grouped_matrix.append(row)

    return grouped_matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


# Input size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Generate random matrix
matrix = [[random.randint(1, 9) for j in range(cols)]
          for i in range(rows)]

print("\nOriginal Matrix:")
print_matrix(matrix)

# Group similar elements
result = group_similar(matrix)

print("\nMatrix with similar elements grouped:")
print_matrix(result)