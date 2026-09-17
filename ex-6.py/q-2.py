def input_matrix():
    matrix = []

    print("Enter 9 elements:")
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    print("\nMatrix:")
    for row in matrix:
        print(*row)


def row_sum(matrix):
    print("\nSum of row elements:")
    for i in range(3):
        total = sum(matrix[i])
        print("Row", i + 1, "=", total)


def column_sum(matrix):
    print("\nSum of column elements:")
    for j in range(3):
        total = 0
        for i in range(3):
            total += matrix[i][j]
        print("Column", j + 1, "=", total)


# Main program
matrix = input_matrix()

print_matrix(matrix)
row_sum(matrix)
column_sum(matrix)
