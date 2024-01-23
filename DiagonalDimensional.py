#"Create a script that creates a two-dimensional array of size 5x5 named 'diagonal'. The elements on its diagonals should be 1, and the rest should be 0. Display the content of the array on the screen."
def create_diagonal_matrix(num_rows, num_cols):
    matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            if row == col or row == (num_rows - 1) - col:
                matrix[row][col] = 1
    return matrix

num_rows = 5
num_cols = 5
matrix = create_diagonal_matrix(num_rows, num_cols)
for row in matrix:
    print(*row)
