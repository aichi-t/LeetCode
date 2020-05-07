def setZeroes(matrix):
    indexes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix[i])):
                    indexes.append([i, k])
                for l in range(len(matrix)):
                    indexes.append([l, j])
    # print(indexes)

    for index in indexes:
        row, col = index
        matrix[row][col] = 0


def setZeroes2(matrix):
    col_zero = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_zero = True
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[i]) - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col_zero:
            matrix[i][0] = 0


if __name__ == "__main__":

    matrix = [[1, 1, 1],  [1, 0, 1], [1, 1, 1]]
    # setZeroes(matrix)
    setZeroes2(matrix)
