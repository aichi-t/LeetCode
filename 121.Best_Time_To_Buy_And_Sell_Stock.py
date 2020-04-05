# Requirement: O(N)

# TODO Solve using Kadane's algorithm


def maxProfit(prices):
    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    """

    if prices == []:
        return 0

    best_profit = 0
    current_min = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < current_min:
            current_min = prices[i]
        else:
            profit = current_min - prices[i]
            if profit < best_profit:
                best_profit = profit

    return abs(best_profit)


# def maxProfit(prices):
#     """
#     Time Complexity : O(N2)
#     """
#     profit = 0
#     for i in range(len(prices)):
#         for j in range(i, len(prices)):
#             if i == j:
#                 continue
#             if prices[i] - prices[j] < profit:
#                 profit = prices[i] - prices[j]
#     return abs(profit)

if __name__ == "__main__":

    prices = [7, 3, 7, 2, 6, 1, 6]
    print(maxProfit(prices))
