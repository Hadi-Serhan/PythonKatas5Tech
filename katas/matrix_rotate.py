def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    # Check if the matrix is empty
    if len(matrix) == 0:
        return matrix
    
    # Matrix is square
    row_len = len(matrix[0])
    col_len = len(matrix[0])
    # Initalize a temp matrix of size matrix so we can append to
    temp_mat = [[0] * col_len for _ in range(row_len)]
    # We iterate over the original matrix rows
    for row in range(0, row_len):
        # Each row "i" should now be in column "len(row) - i - 1", this basically "rotates" the matrix by 90 deg 
        for column in range(0, col_len):
            temp_mat[column][(row_len - row - 1)] = matrix[row][column]
    
    # We copy the rotated temp matrix into the original one
    for row in range(0, row_len):
        for column in range(0, col_len):
            matrix[row][column] = temp_mat[row][column]
    
    return matrix
        


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3
    