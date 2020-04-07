def climbStairs(n):

    stairs = [1, 2]
    if n < 3:
        return stairs[n-1]

    for i in range(2, n):
        stairs.append(stairs[i-1]+stairs[i-2])

    return stairs[-1]


if __name__ == "__main__":
    n = 4
    print(climbStairs(n))
