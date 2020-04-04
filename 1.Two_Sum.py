def two_sum(nums, target):
    '''
    Using a dictionary to map indexes to number value keys.
    '''
    h_map = {}
    for i, num in enumerate(nums):
        if (target-num) in h_map:
            return [i, h_map[target-num]]
        else:
            h_map[num] = i


if __name__ == "__main__":

    target = 6
    nums = [3, 3]
    print(two_sum(nums, target))
