def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


def dfs(board, i, j, word):

    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False

    temp = board[i][j]
    board[i][j] = "#"
    found = dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:]) or dfs(
        board, i-1, j, word[1:]) or dfs(board, i+1, j, word[1:])

    board[i][j] = temp
    return found


if __name__ == "__main__":
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABC"
    print(exist(board, word))
