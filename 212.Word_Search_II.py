class Solution:
    def findWords(self, board, words):
        result = []
        for item in words:
            if self.wordFound(board, item):
                result.append(item)
        return result

    def wordFound(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bfs(board, word, i, j):
                    return True
        return False

    def bfs(self, board, word, i, j):
        if not word:
            return True
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != word[0] or board[i][j] == -1:
            return False
        temp, board[i][j] = board[i][j], -1
        exists = self.bfs(board, word[1:], i+1, j) or self.bfs(board, word[1:], i-1,
                                                               j) or self.bfs(board, word[1:], i, j+1) or self.bfs(board, word[1:], i, j-1)
        board[i][j] = temp
        return exists


if __name__ == "__main__":
    board = [["a", "b"], ["c", "d"]]
    words = ["ab", "cb", "ad", "bd", "ac", "ca", "da",
             "bc", "db", "adcb", "dabc", "abb", "acb"]
    s = Solution()
    print(s.findWords(board, words))
