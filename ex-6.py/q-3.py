def read_matrix(n):
    """Read an n x n matrix from the user."""
    matrix = []
    for i in range(n):
        row = list(map(int, input("Enter row {}: ".format(i + 1)).split()))
        while len(row) != n:
            print("Please enter exactly {} values.".format(n))
            row = list(map(int, input("Enter row {}: ".format(i + 1)).split()))
        matrix.append(row)
    return matrix


def transpose_matrix(matrix):
    """Return the transpose of a square matrix."""
    n = len(matrix)
    return [[matrix[j][i] for j in range(n)] for i in range(n)]


def print_matrix(matrix):
    """Print a matrix row by row."""
    for row in matrix:
        print(*row)


def main():
    n = int(input("Enter the order of the matrix: "))
    if n <= 0:
        print("Order must be a positive integer.")
        return

    matrix = read_matrix(n)
    print("Transpose of the matrix:")
    print_matrix(transpose_matrix(matrix))


if __name__ == "__main__":
    main()