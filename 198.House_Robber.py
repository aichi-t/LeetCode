def rob(nums):
    memo1, memo2 = 0, 0
    for i in range(0, len(nums)):
        if i % 2 == 0:
            memo1 = max(memo1+nums[i], memo2)
        else:
            memo2 = max(memo2+nums[i], memo1)
    return max(memo1, memo2)

    # last, now = 0, 0
    # for num in nums:
    #     last, now = now, (max(last+num), now)
    # return now


if __name__ == "__main__":
    # nums = [1, 2, 3, 1, 1, 5]
    nums = [2, 7, 9, 3, 1]
    rob(nums)
