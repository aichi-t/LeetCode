def wordBreak(s, wordDict):

    dp = [True] + [False] * len(s)

    for i in range(1, len(s)+1):
        for word in wordDict:
            if s[i-len(word):i] == word and dp[i-len(word)]:
                dp[i] = True

    return dp[-1]


if __name__ == "__main__":

    # s = 'catsandog'
    # wordDict = ['cats', 'dog', 'sand', 'and', 'cat']

    # s = 'applepenapple'
    # wordDict = ['apple', 'pen']
    s = 'cars'
    wordDict = ['car', 'ca', 'rs']
    wordBreak(s, wordDict)
