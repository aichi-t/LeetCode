import math


def uniquePaths(m, n):
    return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))


def uniquePaths2(m, n):
    # Dynamic way.
    # 2 ways to reach a grid. Coming down from the top or right from left.
    # That means for a given cell, the number of ways to reach that cell is number of ways to reach top + left
    # O (m*n) space

    dp = [[1 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


def uniquePaths3(m, n):
    # O(m) space 2 rows
    prev = [1 for i in range(m)]
    curr = [1 for i in range(m)]
    for _ in range(1, n):
        for j in range(1, m):
            curr[j] = prev[j] + curr[j-1]
        prev, curr = curr, prev

    return prev[-1]


def uniquePaths4(m, n):
    # O(m) space but 1 row
    dp = [1 for _ in range(m)]
    for _ in range(1, n):
        for j in range(1, m):
            dp[j] += dp[j-1]

    return dp[-1]


if __name__ == "__main__":

    m = 7
    n = 3
    print(uniquePaths(m, n))

    uniquePaths2(m, n)

    uniquePaths3(m, n)

    uniquePaths4(m, n)
