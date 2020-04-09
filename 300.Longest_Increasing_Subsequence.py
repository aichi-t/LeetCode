def lengthOfLIS(nums):
    """ 
    Time Complexity : O(N2)
    Space Complexity : O(2N) = O(N)
    """
    if nums == []:
        return 0

    global_lis = 1
    memo = [[nums[i], 1] for i in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
        lis = 0
        for j in range(i+1, len(nums)):
            if memo[j][0] > nums[i] and memo[j][1] > lis:
                lis = memo[j][1]
        global_lis = max(global_lis, lis+1)
        memo[i][1] = 1+lis

    return(global_lis)

    # if nums == []:
    #     return 0
    # lis = 1
    # for i in range(len(nums)):
    #     num = nums[i]
    #     temp_lis = 1
    #     for j in range(i+1, len(nums)):
    #         if nums[j] > num:
    #             temp_lis += 1
    #             num = nums[j]
    #     lis = max(temp_lis, lis)
    # return lis
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [5, 3, 8, 6, 7, 8]
    # nums = [10, 9, 2, 5, 3, 4]
    print(lengthOfLIS(nums))
