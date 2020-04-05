def containsDuplicate(nums):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    dictionary = {}
    for num in nums:
        if num in dictionary:
            return True
        dictionary[num] = num
    return False

    # Alternative solution using sets from discussions
    # return len(set(nums)) != len(nums)


if __name__ == "__main__":

    nums = [1, 2, 3, 1]  # True
    # nums = [1, 2, 3, 4]  # False

    print(containsDuplicate(nums))
