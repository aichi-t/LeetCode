def threeSum(nums):
    target = 0
    # two pointer scan approach
    nums.sort()
    results = []

    # Three sum at needs at least 3 numbers.
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        partial_target = target - nums[i]

        j = i+1
        k = len(nums) - 1
        while j < k:
            partial_sum = nums[j] + nums[k]
            if partial_sum < partial_target:
                j += 1
            elif partial_sum > partial_target:
                k -= 1
            else:
                results.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
    return results

    # dict = {}
    # results = []
    # for i,num in enumerate(nums):
    #     dict[num] = i
    # for j,num in enumerate(nums):
    #     target = 0-num
    #     for item in dict:
    #         if dict[item] == j:
    #             continue
    #         else:
    #             if target-item in dict:
    #                 if dict[item] != dict[target-item]:
    #                     arr = sorted([num,item,target-item])
    #                     if arr not in results:
    #                         results.append(sorted([num,item,target-item]))
    # return results
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-1,0,1,2,-1,-4]
    # nums = [0, 0, 0, 0]
    print(threeSum(nums))
