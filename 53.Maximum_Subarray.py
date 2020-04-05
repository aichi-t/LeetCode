def maxSubArray(nums):
    # Use Kaden's algorithm.
    global_max = -float('inf')
    local_max = 0
    for num in nums:
        local_max = max(num, local_max+num)
        global_max = max(local_max, global_max)

    return global_max


if __name__ == "__main__":

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Output -> 6

    print(maxSubArray(nums))
