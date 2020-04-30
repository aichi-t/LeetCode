def rotateImage(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swap Horizontally
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    print(matrix)


if __name__ == "__main__":
    matrix = [[1, 2],
              [3, 4]]
    rotateImage(matrix)
