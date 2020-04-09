def combinationSum(nums, target):
    memo = [0] * (target+1)
    for i in range(1, target+1):
        for num in nums:
            if num <= i:
                if num == i:
                    memo[i] += 1
                else:
                    memo[i] += memo[i-num]
    return memo[-1]


if __name__ == "__main__":
    nums = [1, 3]
    target = 4
    combinationSum(nums, target)
