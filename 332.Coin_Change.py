def coinChange(coins, amount):
    memo = [0] + [float('inf')]*amount
    for c in coins:
        for i in range(1, amount+1):
            if i - c >= 0:
                memo[i] = min(memo[i], memo[i-c]+1)

    return memo[-1] if memo[-1] != float('inf') else -1


coins = [1, 2, 5]
amount = 11

coinChange(coins, amount)
