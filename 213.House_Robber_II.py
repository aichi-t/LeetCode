def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    memo1, memo2 = 0, 0
    answer = 0
    for i in range(len(nums)-1):
        memo1, memo2 = memo2, max(memo1+nums[i], memo2)
    answer = max(memo1, memo2)

    memo1, memo2 = 0, 0
    for i in range(1, len(nums)):
        memo1, memo2 = memo2, max(memo1+nums[i], memo2)
    temp_answer = max(memo1, memo2)
    return max(answer, temp_answer)


if __name__ == "__main__":
    # nums = [1, 2, 3, 1, 1, 5]
    nums = [2, 3, 2]
    print(rob(nums))
